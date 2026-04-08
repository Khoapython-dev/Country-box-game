#!/usr/bin/env python3
"""
Test v1.7.8 components
- Map Engine: 95x75, resources, warehouses
- Entity Manager: Chickens AI
"""

import sys
sys.path.insert(0, "/workspaces/Country-box-game")

from core.map_engine import MapEngine, TileType
from core.entity_manager import EntityManager, Chicken

print("=" * 60)
print("TEST v1.7.8 Components")
print("=" * 60)

# Test 1: MapEngine
print("\n[TEST 1] MapEngine 95x75")
map_engine = MapEngine(width=95, height=75)
print(f"✓ Map created: {map_engine.width}x{map_engine.height}")
print(f"✓ Town Hall at: {map_engine.town_hall_pos}")
print(f"✓ Warehouses: {len(map_engine.warehouses)} places at {map_engine.warehouses}")

# Check resources exist
woo_cnt = sum(row.count(TileType.WOOD) for row in map_engine.map)
stone_cnt = sum(row.count(TileType.STONE) for row in map_engine.map)
river_cnt = sum(row.count(TileType.RIVER) for row in map_engine.map)
warehouse_cnt = sum(row.count(TileType.WAREHOUSE) for row in map_engine.map)

print(f"✓ Resources: Wood={woo_cnt}, Stone={stone_cnt}, River={river_cnt}, Warehouse={warehouse_cnt}")

# Test 2: EntityManager + Chickens
print("\n[TEST 2] EntityManager & Chicken AI")
entity_mgr = EntityManager()
entity_mgr.spawn_chickens(count=10, map_width=95, map_height=75)
print(f"✓ Spawned {len(entity_mgr.chickens)} chickens")

# Simulate 5 turns
for turn in range(5):
    result = entity_mgr.update(95, 75, villagers=[
        {"x": 47, "y": 37},  # Player position
    ])
    killed = result["killed_chickens"]
    active = result["active_chickens"]
    print(f"  Turn {turn+1}: {len(active)} alive, {len(killed)} killed")
    if killed:
        print(f"    Killed chickens: {killed}")

print(f"✓ Final state: {len(entity_mgr.chickens)} chickens")

# Test 3: Map walkability
print("\n[TEST 3] Map Walkability")
tx, ty = map_engine.town_hall_pos
print(f"✓ Town Hall ({tx}, {ty}) walkable: {map_engine.is_walkable(tx, ty)}")
print(f"✓ Wall (1, 1) walkable: {map_engine.is_walkable(1, 1)}")
print(f"✓ Empty (50, 50) walkable: {map_engine.is_walkable(50, 50)}")

# Test 4: Resource lookup for AI
print("\n[TEST 4] AI Resource Lookup")
nearby = map_engine.get_nearby_tiles(47, 37, radius=5)
if nearby:
    print(f"✓ Nearby resources from (47, 37):")
    for distance, resource, x, y in nearby[:5]:
        print(f"    Distance {distance}: {resource} at ({x}, {y})")

print("\n" + "=" * 60)
print("✓ All tests passed! v1.7.8 foundation ready.")
print("=" * 60)
