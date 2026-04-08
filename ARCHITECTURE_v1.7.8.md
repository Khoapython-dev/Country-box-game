# v1.7.8 Architecture Plan

## Tổng quan
Chuyển từ CLI đơn giản sang TUI (Textual UI) với map lớn hơn, tài nguyên ngẫu nhiên, công trình mới, động vật.

## Thành phần chính

### 1. UI Layer (Textual)
- **main_screen.py**: Màn hình chính với Textual widgets
  - Hiển thị map 95x75
  - Sidebar: inventory, villager status
  - Log area: messages
  - Main menu trước khi game bắt đầu

### 2. Core Engine (mở rộng từ game.py)
- **game_engine.py**: Logic lõi game
  - Quản lý state game, turn system
  - Gọi logic dân làng, gà, công trình
  
### 3. Entities
- **villager.py**: Tái cấu trúc từ villager.lua
  - Hành động tự động: di chuyển ngẫu nhiên → nhìn xung quanh → khai thác
  - Ăn/uống tự động
  
- **chicken.py**: Động vật gà
  - Di chuyển ngẫu nhiên trên map
  - Nếu gặp dân làng có thể bị giết → +2~3 food
  - Spawn xung quanh map
  
### 4. Map & Resources
- **map_engine.py**: Quản lý map 95x75
  - Tile types: empty, wall, wood, stone, mountain, river, town_hall, warehouse
  - Spam tài nguyên ngẫu nhiên
  - Collision detection
  
### 5. Buildings
- **warehouse.py**: Nhà kho
  - Dung tích max 200 items
  - Spawn 3-4 cái xung quanh town_hall
  - Dân làng tự động đưa tài nguyên vào

### 6. Save/Load (nếu cần)
- **save_manager.py**: Lưu/tải game state

## Quy trình phát triển

### Phase 1: Core (tuần 1)
- [ ] Textual main screen
- [ ] Map engine 95x75
- [ ] Villager simulation (di chuyển + khai thác)
- [ ] Turn system hoạt động

### Phase 2: Content (tuần 2)
- [ ] Warehouse system
- [ ] Chicken AI
- [ ] Resource spawning

### Phase 3: Polish (tuần 3)
- [ ] Main menu
- [ ] Game over (lose condition)
- [ ] Performance optimization

## File Structure
```
Country-box-game/
├── ui/
│   ├── __init__.py
│   ├── main_screen.py
│   └── widgets.py
├── core/
│   ├── game_engine.py (mới)
│   ├── map_engine.py (mới)
│   └── [old files]
├── entities/
│   ├── villager.py (chuyển từ .lua)
│   ├── chicken.py (mới)
│   └── building.py (mới)
├── data/
│   ├── recipe.json
│   └── config.json
└── saves/
    └── [save files]
```

## Ghi chú thiết kế
- Dùng **Textual** cho TUI (terminal UI) chứ không là CLI thuần
- Map 95x75 lớn hơn → cần viewport/camera
- Villager chạy AI riêng, không phụ thuộc lệnh user (tự động)
- Gà chạy AI riêng, có thể bị giết
- Warehouse là tài nguyên quý, giữ tài nguyên khi thoát game
