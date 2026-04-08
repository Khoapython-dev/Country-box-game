"""
chicken.py - Gà động vật cho v1.7.8
- Di chuyển ngẫu nhiên trên map
- Có thể bị giết để lấy thức ăn
- Spawn xung quanh map
"""

import random
from typing import List, Optional, Tuple

class Chicken:
    def __init__(self, cid: int, x: int, y: int):
        self.id = cid
        self.name = f"chicken_{cid}"
        self.x = x
        self.y = y
        self.health = 20  # Dễ giết
        self.alive = True
    
    def update(self, map_engine, messages: List[str]):
        """Cập nhật gà mỗi lượt"""
        if not self.alive:
            return
        
        # Di chuyển ngẫu nhiên
        if random.random() < 0.7:  # 70% di chuyển
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            new_x, new_y = self.x + dx, self.y + dy
            if map_engine.is_walkable(new_x, new_y):
                self.x = new_x
                self.y = new_y
    
    def take_damage(self, damage: int) -> bool:
        """Nhận sát thương. Trả về True nếu chết"""
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            return True
        return False
    
    def kill(self) -> int:
        """Giết gà, trả về food"""
        self.alive = False
        return random.randint(2, 4)  # 2-4 food
    
    def __repr__(self):
        return f"{self.name}(pos=({self.x},{self.y}), health={self.health})"


class ChickenManager:
    def __init__(self, count: int = 5):
        self.chickens: List[Chicken] = []
        self.create_chickens(count)
    
    def create_chickens(self, count: int):
        """Spawn gà ngẫu nhiên trên map"""
        for i in range(count):
            x = random.randint(10, 84)
            y = random.randint(10, 64)
            self.chickens.append(Chicken(i, x, y))
    
    def update_all(self, map_engine, messages: List[str]):
        """Cập nhật tất cả gà"""
        for c in self.chickens:
            if c.alive:
                c.update(map_engine, messages)
    
    def get_alive_count(self) -> int:
        """Đếm gà sống sót"""
        return sum(1 for c in self.chickens if c.alive)
    
    def kill_at(self, x: int, y: int) -> Optional[int]:
        """
        Cố gắng giết gà tại vị trí.
        Trả về food lấy được, hoặc None nếu không có gà.
        """
        for c in self.chickens:
            if c.alive and c.x == x and c.y == y:
                food = c.kill()
                return food
        return None
    
    def get_status_report(self) -> str:
        """Báo cáo tình trạng gà"""
        alive = self.get_alive_count()
        return f"Chickens: {alive}/{len(self.chickens)} alive"
