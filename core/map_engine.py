"""
map_engine.py - Quản lý map 95x75 cho v1.7.8
- Tile types, spawn tài nguyên ngẫu nhiên
- Hỗ trợ collision, pathfinding cơ bản
"""

import random
from enum import IntEnum
from typing import List, Tuple, Optional

# Tile types
class TileType(IntEnum):
    EMPTY = 0        # .
    WALL = 1         # #
    WOOD = 2         # 🌲
    STONE = 3        # 🪨
    MOUNTAIN = 4     # ⛰️
    RIVER = 5        # 🏞️
    TOWN_HALL = 6    # 🏰
    WAREHOUSE = 7    # 🛖
    GRASS = 8        # Grass (placeholder, optional)

TILE_DISPLAY = {
    TileType.EMPTY: ".",
    TileType.WALL: "#",
    TileType.WOOD: "🌲",
    TileType.STONE: "🪨",
    TileType.MOUNTAIN: "⛰️",
    TileType.RIVER: "🏞️",
    TileType.TOWN_HALL: "🏰",
    TileType.WAREHOUSE: "🛖",
    TileType.GRASS: "·",
}

class MapEngine:
    def __init__(self, width: int = 95, height: int = 75):
        self.width = width
        self.height = height
        self.map: List[List[TileType]] = [[TileType.EMPTY for _ in range(width)] for _ in range(height)]
        self.town_hall_pos: Tuple[int, int] = (width // 2, height // 2)
        self.warehouses: List[Tuple[int, int]] = []
        
        # Initialize
        self._init_borders()
        self._place_town_hall()
        self._place_warehouses()
        self._spawn_resources()
        self._spawn_terrain()
    
    def _init_borders(self):
        """Tạo tường xung quanh map"""
        for y in range(self.height):
            self.map[y][0] = TileType.WALL
            self.map[y][self.width - 1] = TileType.WALL
        for x in range(self.width):
            self.map[0][x] = TileType.WALL
            self.map[self.height - 1][x] = TileType.WALL
    
    def _place_town_hall(self):
        """Đặt toà thị chính ở trung tâm"""
        x, y = self.town_hall_pos
        self.map[y][x] = TileType.TOWN_HALL
    
    def _place_warehouses(self, count: int = 4):
        """Spam 3-4 nhà kho xung quanh town_hall"""
        tx, ty = self.town_hall_pos
        directions = [(-5, -5), (5, -5), (-5, 5), (5, 5)]
        
        random.shuffle(directions)
        for i in range(min(count, len(directions))):
            dx, dy = directions[i]
            wx, wy = tx + dx, ty + dy
            # Đảm bảo trong biên
            wx = max(2, min(self.width - 3, wx))
            wy = max(2, min(self.height - 3, wy))
            
            if self.is_valid(wx, wy):
                self.map[wy][wx] = TileType.WAREHOUSE
                self.warehouses.append((wx, wy))
    
    def _spawn_resources(self):
        """Spam ngẫu nhiên tài nguyên (gỗ, đá)"""
        # Spam wood
        for _ in range(200):  # 200 cây
            x = random.randint(2, self.width - 3)
            y = random.randint(2, self.height - 3)
            if self.is_walkable(x, y):
                self.map[y][x] = TileType.WOOD
        
        # Spam stone
        for _ in range(200):  # 200 đá
            x = random.randint(2, self.width - 3)
            y = random.randint(2, self.height - 3)
            if self.is_walkable(x, y):
                self.map[y][x] = TileType.STONE
    
    def _spawn_terrain(self):
        """Spam núi và sông ngẫu nhiên"""
        # Mountains
        for _ in range(50):
            x = random.randint(2, self.width - 3)
            y = random.randint(2, self.height - 3)
            if self.is_walkable(x, y):
                self.map[y][x] = TileType.MOUNTAIN
        
        # Rivers (lines)
        for _ in range(5):
            start_x = random.randint(1, self.width - 2)
            start_y = random.randint(1, self.height - 2)
            # Vẽ một dòng sông ngẫu nhiên
            for step in range(random.randint(5, 15)):
                x = start_x + step
                y = start_y + random.randint(-2, 2)
                if self.is_valid(x, y) and self.is_walkable(x, y):
                    self.map[y][x] = TileType.RIVER
    
    def get_tile(self, x: int, y: int) -> TileType:
        """Lấy tile type tại vị trí"""
        if not self.is_valid(x, y):
            return TileType.WALL
        return self.map[y][x]
    
    def set_tile(self, x: int, y: int, tile_type: TileType) -> bool:
        """Đặt tile type tại vị trí"""
        if not self.is_valid(x, y):
            return False
        self.map[y][x] = tile_type
        return True
    
    def is_valid(self, x: int, y: int) -> bool:
        """Kiểm tra vị trí có trong map không"""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def is_walkable(self, x: int, y: int) -> bool:
        """Kiểm tra ô có thể đi bộ không (không là tường, núi)"""
        if not self.is_valid(x, y):
            return False
        tile = self.get_tile(x, y)
        return tile not in [TileType.WALL, TileType.MOUNTAIN]
    
    def is_harvestable(self, x: int, y: int) -> Optional[str]:
        """
        Kiểm tra ô có tài nguyên khai thác không.
        Trả về tên tài nguyên hoặc None.
        """
        tile = self.get_tile(x, y)
        if tile == TileType.WOOD:
            return "wood"
        elif tile == TileType.STONE:
            return "stone"
        elif tile == TileType.RIVER:
            return "water"
        return None
    
    def harvest(self, x: int, y: int) -> Optional[str]:
        """
        Khai thác tài nguyên tại vị trí.
        Trả về tên tài nguyên hoặc None.
        Sông không biến mất, cây/đá thành ô trống.
        """
        tile = self.get_tile(x, y)
        if tile == TileType.WOOD:
            self.set_tile(x, y, TileType.EMPTY)
            return "wood"
        elif tile == TileType.STONE:
            self.set_tile(x, y, TileType.EMPTY)
            return "stone"
        elif tile == TileType.RIVER:
            return "water"  # Sông không biến mất
        return None
    
    def get_neighbors(self, x: int, y: int, range_: int = 1) -> List[Tuple[int, int]]:
        """Lấy danh sách ô lân cận"""
        neighbors = []
        for dx in range(-range_, range_ + 1):
            for dy in range(-range_, range_ + 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny):
                    neighbors.append((nx, ny))
        return neighbors
    
    def render_viewport(self, center_x: int, center_y: int, width: int = 60, height: int = 30) -> str:
        """
        Render một phần map (viewport) với camera ở center.
        Dùng cho display trong TUI.
        """
        half_w, half_h = width // 2, height // 2
        lines = []
        
        for y in range(center_y - half_h, center_y + half_h):
            line = ""
            for x in range(center_x - half_w, center_x + half_w):
                if self.is_valid(x, y):
                    if x == center_x and y == center_y:
                        line += "@"  # Player
                    else:
                        tile = self.get_tile(x, y)
                        line += TILE_DISPLAY.get(tile, "?")
                else:
                    line += " "
            lines.append(line)
        
        return "\n".join(lines)
