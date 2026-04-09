"""
Map render và logic cho Country Box v2.0.
- Hỗ trợ map lớn 90x75 với viewport rendering
- Sử dụng mã số (int) để biểu diễn tile
- Render ra emoji khi display
- Tối ưu performance với viewport system
"""

import random

# Tile types: dùng số thay vì emoji để tránh vấn đề indexing với multi-byte character
TILE_EMPTY = 0        # .
TILE_WALL = 1         # #
TILE_WOOD = 2         # 🌲
TILE_STONE = 3        # 🪨
TILE_MOUNTAIN = 4     # ⛰️
TILE_RIVER = 5        # 🏞️
TILE_TOWN_HALL = 6    # 🏰
TILE_VILLAGE = 7      # 🏘️ (cho multi-village)

# Mapping để render
TILE_DISPLAY = {
    TILE_EMPTY: ".",
    TILE_WALL: "#",
    TILE_WOOD: "🌲",
    TILE_STONE: "🪨",
    TILE_MOUNTAIN: "⛰️",
    TILE_RIVER: "🏞️",
    TILE_TOWN_HALL: "🏰",
    TILE_VILLAGE: "🏘️",
}

# Map dimensions
MAP_WIDTH = 90
MAP_HEIGHT = 75

def generate_large_map():
    """Tạo map 90x75 với tài nguyên ngẫu nhiên"""
    # Khởi tạo map với empty tiles
    map_data = [[TILE_EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    # Thêm walls xung quanh biên
    for x in range(MAP_WIDTH):
        map_data[0][x] = TILE_WALL
        map_data[MAP_HEIGHT-1][x] = TILE_WALL
    for y in range(MAP_HEIGHT):
        map_data[y][0] = TILE_WALL
        map_data[y][MAP_WIDTH-1] = TILE_WALL

    # Thêm town hall ở center
    center_x, center_y = MAP_WIDTH // 2, MAP_HEIGHT // 2
    map_data[center_y][center_x] = TILE_TOWN_HALL

    # Thêm rivers (sông)
    for _ in range(5):
        river_start = random.randint(5, MAP_WIDTH-5)
        river_length = random.randint(20, 40)
        direction = random.choice(['horizontal', 'vertical'])

        if direction == 'horizontal':
            y = random.randint(5, MAP_HEIGHT-5)
            for x in range(max(1, river_start-10), min(MAP_WIDTH-1, river_start+10)):
                if random.random() < 0.7:  # 70% chance to place river
                    map_data[y][x] = TILE_RIVER
        else:
            x = random.randint(5, MAP_WIDTH-5)
            for y in range(max(1, river_start-10), min(MAP_HEIGHT-1, river_start+10)):
                if random.random() < 0.7:
                    map_data[y][x] = TILE_RIVER

    # Thêm mountains (núi)
    for _ in range(15):
        mountain_x = random.randint(5, MAP_WIDTH-5)
        mountain_y = random.randint(5, MAP_HEIGHT-5)
        # Tạo cluster núi
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                x, y = mountain_x + dx, mountain_y + dy
                if 1 <= x < MAP_WIDTH-1 and 1 <= y < MAP_HEIGHT-1:
                    if random.random() < 0.4:
                        map_data[y][x] = TILE_MOUNTAIN

    # Thêm wood và stone clusters
    for _ in range(30):  # wood clusters
        wood_x = random.randint(5, MAP_WIDTH-5)
        wood_y = random.randint(5, MAP_HEIGHT-5)
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                x, y = wood_x + dx, wood_y + dy
                if 1 <= x < MAP_WIDTH-1 and 1 <= y < MAP_HEIGHT-1:
                    if map_data[y][x] == TILE_EMPTY and random.random() < 0.6:
                        map_data[y][x] = TILE_WOOD

    for _ in range(20):  # stone clusters
        stone_x = random.randint(5, MAP_WIDTH-5)
        stone_y = random.randint(5, MAP_HEIGHT-5)
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                x, y = stone_x + dx, stone_y + dy
                if 1 <= x < MAP_WIDTH-1 and 1 <= y < MAP_HEIGHT-1:
                    if map_data[y][x] == TILE_EMPTY and random.random() < 0.5:
                        map_data[y][x] = TILE_STONE

    return map_data

# Global map instance
MAP = generate_large_map()

# vị trí toà thị chính ở trung tâm
TOWN_HALL_POS = (MAP_WIDTH // 2, MAP_HEIGHT // 2)  # x, y


def render_viewport(player_x, player_y, viewport_width=80, viewport_height=20):
    """
    Render map với viewport xung quanh player.
    Trả về string để Textual UI hiển thị.
    """
    # Tính viewport bounds
    half_vw = viewport_width // 2
    half_vh = viewport_height // 2

    start_x = max(0, player_x - half_vw)
    end_x = min(MAP_WIDTH, player_x + half_vw + 1)
    start_y = max(0, player_y - half_vh)
    end_y = min(MAP_HEIGHT, player_y + half_vh + 1)

    # Tạo display map cho viewport
    display_lines = []

    for y in range(start_y, end_y):
        line = ""
        for x in range(start_x, end_x):
            if x == player_x and y == player_y:
                line += "@"  # Player
            elif x == TOWN_HALL_POS[0] and y == TOWN_HALL_POS[1]:
                line += TILE_DISPLAY[TILE_TOWN_HALL]  # Town hall
            else:
                tile = MAP[y][x]
                line += TILE_DISPLAY.get(tile, "?")
        display_lines.append(line)

    return "\n".join(display_lines)


def render_full_map(player_x, player_y):
    """
    Render toàn bộ map (cho debug hoặc CLI fallback).
    """
    import os
    try:
        os.system('clear')  # Linux/Mac
    except:
        os.system('cls')    # Windows fallback

    # Render từng dòng
    for y in range(MAP_HEIGHT):
        line = ""
        for x in range(MAP_WIDTH):
            if x == player_x and y == player_y:
                line += "@"
            elif x == TOWN_HALL_POS[0] and y == TOWN_HALL_POS[1]:
                line += TILE_DISPLAY[TILE_TOWN_HALL]
            else:
                tile = MAP[y][x]
                line += TILE_DISPLAY.get(tile, "?")
        print(line)


def get_tile(x, y):
    """Lấy loại tile ở vị trí (x, y)."""
    if 0 <= y < MAP_HEIGHT and 0 <= x < MAP_WIDTH:
        return MAP[y][x]
    return TILE_WALL  # Out of bounds = wall


def is_walkable(x, y):
    """Kiểm tra tile có thể đi được không."""
    tile = get_tile(x, y)
    return tile not in [TILE_WALL, TILE_MOUNTAIN]


def harvest_tile(x, y):
    """Thu hoạch tài nguyên ở vị trí (x, y)."""
    tile = get_tile(x, y)
    if tile == TILE_WOOD:
        MAP[y][x] = TILE_EMPTY  # Xóa wood sau khi harvest
        return "wood"
    elif tile == TILE_STONE:
        MAP[y][x] = TILE_EMPTY  # Xóa stone sau khi harvest
        return "stone"
    elif tile == TILE_RIVER:
        return "water"  # River không bị xóa
    return None


def get_map_info():
    """Trả về thông tin về map."""
    wood_count = sum(row.count(TILE_WOOD) for row in MAP)
    stone_count = sum(row.count(TILE_STONE) for row in MAP)
    mountain_count = sum(row.count(TILE_MOUNTAIN) for row in MAP)
    river_count = sum(row.count(TILE_RIVER) for row in MAP)

    return {
        "dimensions": f"{MAP_WIDTH}x{MAP_HEIGHT}",
        "wood_clusters": wood_count,
        "stone_clusters": stone_count,
        "mountains": mountain_count,
        "rivers": river_count,
        "town_hall": TOWN_HALL_POS
    }
    return TILE_WALL


def is_walkable(x, y):
    """Kiểm tra ô có thể đi vào không."""
    tile = get_tile(x, y)
    return tile not in [TILE_WALL, TILE_MOUNTAIN]


def harvest_tile(x, y):
    """
    Thu thập tài nguyên ở ô (x, y).
    Trả về loại tài nguyên hoặc None nếu không có gì.
    """
    tile = get_tile(x, y)
    if tile == TILE_WOOD:
        MAP[y][x] = TILE_EMPTY
        return "wood"
    elif tile == TILE_STONE:
        MAP[y][x] = TILE_EMPTY
        return "stone"
    elif tile == TILE_RIVER:
        # Sông không biến mất, nhưng cho lấy nước
        return "water"
    return None


def has_nearby_river(x, y):
    """Kiểm tra có sông gần vị trí (x, y) không."""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if get_tile(x + dx, y + dy) == TILE_RIVER:
                return True
    return False