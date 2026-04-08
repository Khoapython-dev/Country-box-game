"""
villager.py - Logic dân làng cho v1.7.8
- Di chuyển ngẫu nhiên xung quanh
- Tự động khai thác tài nguyên xung quanh
- Tự động ăn/uống
- AI đơn giản nhưng thông minh
"""

import random
from enum import Enum
from typing import Optional, Tuple, List

class VillagerStatus(Enum):
    IDLE = "idle"
    MOVING = "moving"
    HARVESTING = "harvesting"
    EATING = "eating"
    DRINKING = "drinking"
    DEAD = "dead"

class Villager:
    def __init__(self, vid: int, x: int, y: int):
        self.id = vid
        self.name = f"villager_{vid}"
        self.x = x
        self.y = y
        
        # Stats
        self.hunger = 50
        self.thirst = 50
        self.health = 100
        
        # Status
        self.status = VillagerStatus.IDLE
        self.target_x: Optional[int] = None
        self.target_y: Optional[int] = None
        
        # Inventory
        self.carrying: dict = {"food": 0, "water": 0, "wood": 0, "stone": 0}
        self.carry_limit = 10
    
    def update(self, map_engine, inventory_game: dict, messages: List[str]):
        """
        Cập nhật villager mỗi lượt.
        Thực hiện các hành động tự động.
        """
        # Kiểm tra sống
        if self.hunger <= 0 or self.thirst <= 0 or self.health <= 0:
            self.status = VillagerStatus.DEAD
            return
        
        # Tăng đói/khát
        self.hunger = max(0, self.hunger - 3)
        self.thirst = max(0, self.thirst - 3)
        
        # Nếu quá đói, ăn từ carrying hoặc game inventory
        if self.hunger < 20:
            if self.carrying["food"] > 0:
                self.carrying["food"] -= 1
                self.hunger = min(100, self.hunger + 30)
                self.status = VillagerStatus.EATING
                messages.append(f"{self.name} ăn thức ăn từ backpack.")
                return
            elif inventory_game.get("food", 0) > 0:
                inventory_game["food"] -= 1
                self.hunger = min(100, self.hunger + 30)
                self.status = VillagerStatus.EATING
                messages.append(f"{self.name} ăn thức ăn từ kho.")
                return
        
        # Nếu quá khát, uống
        if self.thirst < 20:
            if self.carrying["water"] > 0:
                self.carrying["water"] -= 1
                self.thirst = min(100, self.thirst + 30)
                self.status = VillagerStatus.DRINKING
                messages.append(f"{self.name} uống nước.")
                return
            elif inventory_game.get("water", 0) > 0:
                inventory_game["water"] -= 1
                self.thirst = min(100, self.thirst + 30)
                self.status = VillagerStatus.DRINKING
                messages.append(f"{self.name} uống nước từ kho.")
                return
        
        # Tìm tài nguyên xung quanh
        for nx, ny in map_engine.get_neighbors(self.x, self.y, range_=2):
            harvestable = map_engine.is_harvestable(nx, ny)
            if harvestable:
                # Di chuyển đến ô đó
                if sum(self.carrying.values()) < self.carry_limit:
                    self.move_towards(nx, ny)
                    return
        
        # Nếu không thấy tài nguyên, di chuyển ngẫu nhiên
        if random.random() < 0.5:  # 50% di chuyển mỗi lượt
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            new_x, new_y = self.x + dx, self.y + dy
            if map_engine.is_walkable(new_x, new_y):
                self.x = new_x
                self.y = new_y
                self.status = VillagerStatus.MOVING
    
    def move_towards(self, target_x: int, target_y: int):
        """Di chuyển một bước gần hơn đến target"""
        dx = 0 if self.x == target_x else (1 if target_x > self.x else -1)
        dy = 0 if self.y == target_y else (1 if target_y > self.y else -1)
        
        new_x = self.x + dx
        new_y = self.y + dy
        
        self.x = new_x
        self.y = new_y
    
    def try_harvest(self, map_engine, inventory_game: dict, messages: List[str]):
        """Thử khai thác tài nguyên tại vị trí chân"""
        result = map_engine.harvest(self.x, self.y)
        if result:
            if sum(self.carrying.values()) < self.carry_limit:
                self.carrying[result] += 1
                self.status = VillagerStatus.HARVESTING
                messages.append(f"{self.name} khai thác {result} tại ({self.x}, {self.y}).")
            else:
                # Backpack đầy, đổ vào inventory_game
                for key in self.carrying:
                    if self.carrying[key] > 0:
                        inventory_game[key] += self.carrying[key]
                self.carrying[key] = 0
                messages.append(f"{self.name} kho đầy, đưa tất cả vào kho.")
    
    def to_dict(self) -> dict:
        """Serialize villager để lưu"""
        return {
            "id": self.id,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "health": self.health,
            "status": self.status.value,
            "carrying": self.carrying,
        }
    
    def __repr__(self):
        return f"{self.name}(pos=({self.x},{self.y}), hunger={self.hunger}, thirst={self.thirst}, status={self.status})"


class VillagerManager:
    def __init__(self, count: int = 10):
        self.villagers: List[Villager] = []
        self.create_villagers(count, 47, 37)  # Tạo ở town hall
    
    def create_villagers(self, count: int, start_x: int, start_y: int):
        """Tạo dân làng xung quanh town hall"""
        for i in range(count):
            # Scatter xung quanh town hall
            x = start_x + random.randint(-3, 3)
            y = start_y + random.randint(-3, 3)
            self.villagers.append(Villager(i, x, y))
    
    def update_all(self, map_engine, inventory_game: dict, messages: List[str]):
        """Cập nhật tất cả villagers"""
        for v in self.villagers:
            if v.status != VillagerStatus.DEAD:
                v.update(map_engine, inventory_game, messages)
        
        # Cố gắng khai thác tài nguyên dưới chân
        for v in self.villagers:
            if map_engine.is_harvestable(v.x, v.y):
                v.try_harvest(map_engine, inventory_game, messages)
    
    def get_alive_count(self) -> int:
        """Đếm dân làng sống sót"""
        return sum(1 for v in self.villagers if v.status != VillagerStatus.DEAD)
    
    def get_status_report(self) -> str:
        """Báo cáo tình trạng dân làng"""
        alive = self.get_alive_count()
        hungry = sum(1 for v in self.villagers if v.hunger < 20 and v.status != VillagerStatus.DEAD)
        thirsty = sum(1 for v in self.villagers if v.thirst < 20 and v.status != VillagerStatus.DEAD)
        
        return f"Villagers: {alive}/10 alive | {hungry} hungry | {thirsty} thirsty"
