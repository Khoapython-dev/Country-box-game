# v2.0 Architecture Plan - Country Box Game

## Tổng quan
Game mô phỏng làng xã với CLI interface, tập trung vào quản lý tài nguyên, dân số, và sự kiện ngẫu nhiên. Tuân thủ AGENTLAW: code sạch, tổ chức file rõ ràng, entities dùng Lua.

## Trạng thái hiện tại (v2.0.0)
- ✅ Textual UI framework integration
- ✅ Map expansion 20x18 → 90x75 với procedural generation
- ✅ Viewport rendering system (80x20 viewport)
- ✅ Real-time UI components (status, messages, commands)
- ✅ Population System: sinh sản + chết đói
- ✅ Event System: 8 events ngẫu nhiên từ JSON
- ✅ Trade system với merchants
- ✅ Role system: 4 loại villagers với bonus
- ✅ Tech tree: smelter, iron, steel, tools
- ✅ Threat system: wolves, bandits
- ✅ Weather & day/night cycle

## Thành phần chính

### 1. UI Layer (Textual)
- **ui/main.py**: Textual App chính
  - CountryBoxApp: Main application class
  - MapView: Viewport rendering cho map 90x75
  - StatusPanel: Real-time game status
  - MessageLog: Event history
  - CommandInput: Interactive command input

- **ui/__init__.py**: Package initialization

### 2. Core Engine (Python)
- **core/game.py**: Engine chính
  - Game state management (dict-based)
  - Turn logic: population, events, weather, threats
  - Command processing
  - Status reporting

- **core/commands.py**: Command parser
  - Parse user input thành actions
  - Help system

- **core/map_render.py**: Map system
  - 90x75 map generation với procedural content
  - Viewport rendering cho performance
  - Resource harvesting logic
  - Collision detection

### 3. Data Layer (JSON configs)
- **data/events.json**: Event definitions với probability, conditions, effects
- **data/recipe.json**: Crafting recipes
- **data/diplomacy.json**: Multi-village diplomacy data

### 4. Entities (Lua scripts)
- **entities/villager.lua**: Villager behavior (hunger, thirst, movement)
- **entities/chicken.lua**: Chicken AI (movement, spawning, food drops)

### 5. Mods (Lua scripts)
- **mods/public/example.lua**: Example mod structure

## Quy trình phát triển (AGENTLAW compliant)

### Phase 1: Core Foundation ✅ (Đã hoàn thành)
- [x] Basic CLI game loop
- [x] Resource management (food, water, wood, stone, iron, steel)
- [x] Villager roles & harvesting
- [x] Weather & time system
- [x] Threat system

### Phase 2: Population & Events ✅ (Đã hoàn thành)
- [x] Population growth mechanics
- [x] Starvation death system
- [x] Event System JSON
- [x] Trade with merchants
- [x] Random disasters & blessings

### Phase 2.5: Textual UI Migration ✅ (Đã hoàn thành)
- [x] Textual framework integration với conditional imports
- [x] Map expansion 20x18 → 90x75 với procedural generation
- [x] Viewport rendering system (80x20 viewport) với performance optimization
- [x] Real-time UI components (status, messages, commands)
- [x] Command input interface với auto-clear và error handling
- [x] UI testing & validation suite
- [x] CLI fallback system khi Textual unavailable
- [x] Demo script cho non-interactive testing

### Phase 3: Diplomacy & Multi-village (Sắp tới)
- [ ] Village relationships (ally, neutral, enemy)
- [ ] Trade between villages
- [ ] Raids & alliances
- [ ] Multi-village map expansion

### Phase 4: Advanced Features
- [ ] Save/Load system
- [ ] Mod support (Lua scripting)
- [ ] Advanced AI villagers
- [ ] Building construction system
- [ ] Technology research tree expansion

### Phase 5: Polish & Performance
- [ ] UI improvements
- [ ] Performance optimization
- [ ] Tutorial system
- [ ] Achievement system
- [ ] Multiplayer support (future)

## File Structure (AGENTLAW compliant)
```
Country-box-game/
├── core/                    # Python engine code
│   ├── __init__.py
│   ├── game.py             # Main game engine
│   ├── commands.py         # Command parsing
│   └── map_render.py       # Map display & movement
├── data/                   # JSON configs (theo AGENTLAW)
│   ├── events.json         # Event definitions
│   ├── recipe.json         # Crafting recipes
│   └── diplomacy.json      # Multi-village data
├── entities/               # Lua entities (theo AGENTLAW)
│   ├── villager.lua        # Villager AI
│   └── chicken.lua         # Chicken AI
├── mods/                   # Lua mods (theo AGENTLAW)
│   └── public/
│       └── example.lua
├── README.md               # Documentation
├── AGENTLAW.md            # Development rules
└── ARCHITECTURE_v2.0.md   # This file
```

## Ghi chú thiết kế
- **CLI-first**: Giữ đơn giản, tập trung gameplay trước UI
- **Dict-based state**: Dễ serialize, không cần ORM phức tạp
- **Lua entities**: Dễ modding, tách logic AI ra khỏi Python core
- **JSON configs**: Dễ chỉnh sửa events/recipes mà không code
- **Turn-based**: Mỗi action = 1 turn, cho phép suy nghĩ chiến lược
- **AGENTLAW compliance**: Code sạch, test trước khi commit, tổ chức file theo quy tắc

## Metrics thành công
- Population system hoạt động: villagers tăng từ 10 → 15+ qua 50 turns
- Event system trigger: 5+ events trong 50 turns test
- Trade system functional: mua/bán với merchants
- Code quality: Tuân thủ AGENTLAW, không code dỡ
- Performance: <1s per turn, CLI responsive
