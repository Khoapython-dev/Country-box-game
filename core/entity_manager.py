"""
Entity Manager - quản lý tất cả entities (gà, động vật khác)
Logic gà được port từ entities/chicken.lua
"""

import random
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Chicken:
    """
    Con gà - động vật di chuyển ngẫu nhiên trên map.
    - Di chuyển sau mỗi 2 lượt
    - Nếu gặp dân làng có 50% chance bị giết
    - Cho 2-3 food khi bị giết
    """
    x: int
    y: int
    id: int = field(default_factory=lambda: random.randint(1, 1000000))
    hunger: int = 50
    alive: bool = True
    last_move: int = 0

    def move_random(self, map_width: int, map_height: int):
        """Di chuyển ngẫu nhiên, logic từ chicken.lua"""
        if not self.alive:
            return

        self.last_move += 1
        if self.last_move < 2:
            return
        self.last_move = 0

        # Chọn hướng: up, down, left, right
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dx, dy = random.choice(directions)
        new_x, new_y = self.x + dx, self.y + dy

        # Check bounds
        if 0 <= new_x < map_width and 0 <= new_y < map_height:
            self.x = new_x
            self.y = new_y

        # Độ đói tăng
        self.hunger = max(0, self.hunger - 2)

    def check_collision_with_villager(self, vx: int, vy: int) -> Tuple[bool, int]:
        """
        Kiểm tra có va chạm với dân làng không.
        Nếu đúng và may mắn (50%), gà bị giết.
        Return: (was_killed, food_gained)
        """
        if not self.alive:
            return False, 0

        distance = ((self.x - vx) ** 2 + (self.y - vy) ** 2) ** 0.5
        if distance < 2:  # Gần dân làng
            if random.random() < 0.5:  # 50% chance
                self.alive = False
                return True, random.randint(2, 3)

        return False, 0


class EntityManager:
    """Quản lý tất cả entities trên map"""

    def __init__(self):
        self.chickens: List[Chicken] = []

    def spawn_chickens(self, count: int, map_width: int, map_height: int):
        """Spawn `count` gà ngẫu nhiên trên map"""
        for _ in range(count):
            x = random.randint(5, map_width - 5)
            y = random.randint(5, map_height - 5)
            self.chickens.append(Chicken(x, y))

    def update(self, map_width: int, map_height: int, villagers: List = None) -> dict:
        """
        Cập nhật tất cả entities.
        - Gà di chuyển
        - Check va chạm với dân làng

        Return: {
            "killed_chickens": [list of (x, y, food_gained)],
            "active_chickens": [list of (x, y, id)]
        }
        """
        killed = []
        villager_poses = {(v["x"], v["y"]) for v in (villagers or [])}

        for chicken in self.chickens[:]:
            if not chicken.alive:
                self.chickens.remove(chicken)
                continue

            chicken.move_random(map_width, map_height)

            # Check va chạm
            for vx, vy in villager_poses:
                was_killed, food = chicken.check_collision_with_villager(vx, vy)
                if was_killed:
                    killed.append((chicken.x, chicken.y, food))
                    break

        return {
            "killed_chickens": killed,
            "active_chickens": [
                {"x": c.x, "y": c.y, "id": c.id, "hunger": c.hunger}
                for c in self.chickens
                if c.alive
            ],
        }

    def get_all_positions(self) -> list:
        """Lấy vị trí tất cả gà để render"""
        return [(c.x, c.y) for c in self.chickens if c.alive]
