# Phase 3: Diplomacy & Multi-village System

## Tổng quan
Mở rộng game từ single village sang multi-village world với diplomacy, trade, và conflicts.

## Thành phần chính

### 1. Village System
- **data/diplomacy.json**: Village relationships, trade agreements
- **core/diplomacy.py**: Diplomacy engine
  - Relationship states: Ally, Neutral, Enemy
  - Trade negotiations
  - Raid mechanics
  - Alliance formations

### 2. Multi-village Map
- **core/map_render.py** (extend): Multiple village locations
- Town hall markers cho mỗi village
- Trade routes visualization
- Border territories

### 3. Trade System Enhancement
- Inter-village trade caravans
- Resource exchange rates
- Trade agreements & treaties
- Merchant NPC movements between villages

### 4. Conflict System
- Raid mechanics (send villagers to attack)
- Defense bonuses
- Casualty calculations
- War declarations & peace treaties

### 5. AI Villages
- **entities/village_ai.lua**: Village AI behavior
- Resource management AI
- Diplomacy decision making
- Expansion strategies

## Implementation Steps

### Step 1: Core Diplomacy Engine
- [ ] Create core/diplomacy.py
- [ ] Define relationship states & transitions
- [ ] Basic trade mechanics

### Step 2: Multi-village Map Generation
- [ ] Extend map_render.py for multiple villages
- [ ] Village placement algorithm
- [ ] Distance calculations

### Step 3: Trade & Raids
- [ ] Inter-village trade commands
- [ ] Raid command implementation
- [ ] Combat resolution system

### Step 4: AI Villages
- [ ] Basic village AI script
- [ ] Decision making logic
- [ ] Resource allocation AI

### Step 5: UI Integration
- [ ] Diplomacy panel in Textual UI
- [ ] Village status displays
- [ ] Trade negotiation interface

## Files to Create/Modify
- `core/diplomacy.py` (new)
- `data/diplomacy.json` (extend)
- `entities/village_ai.lua` (new)
- `core/map_render.py` (modify)
- `core/commands.py` (extend)
- `ui/main.py` (extend)

## Testing Strategy
- Unit tests cho diplomacy logic
- Integration tests cho multi-village interactions
- UI tests cho diplomacy panels
- Performance tests với multiple villages