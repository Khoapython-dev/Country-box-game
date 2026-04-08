"""
map render và logic đơn giản cho Country Box v1.4.
- Sử dụng mã số (int) để biểu diễn tile trong MAP, tránh lỗi emoji multi-byte.
- Render ra emoji khi display.
- Dễ mở rộng, debug, và performance tốt hơn.
"""

# Tile types: dùng số thay vì emoji để tránh vấn đề indexing với multi-byte character
TILE_EMPTY = 0        # .
TILE_WALL = 1         # #
TILE_WOOD = 2         # 🌲
TILE_STONE = 3        # 🪨
TILE_MOUNTAIN = 4     # ⛰️
TILE_RIVER = 5        # 🏞️
TILE_TOWN_HALL = 6    # 🏰

# Mapping để render
TILE_DISPLAY = {
    TILE_EMPTY: ".",
    TILE_WALL: "#",
    TILE_WOOD: "🌲",
    TILE_STONE: "🪨",
    TILE_MOUNTAIN: "⛰️",
    TILE_RIVER: "🏞️",
    TILE_TOWN_HALL: "🏰",
}

# Bản đồ 20x18 dùng số vì performance và indexing accuracy
MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # tường trên
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,2,0,0,3,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,1],
    [1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # tường dưới
]

# vị trí toà thị chính ở trung tâm
TOWN_HALL_POS = (10, 9)  # x, y


def render(player_x, player_y):
    """
    Render map với player position.
    Chuyển MAP (dùng số) thành display (dùng emoji).
    """
    import os
    try:
        os.system('clear')  # Linux/Mac
    except:
        os.system('cls')    # Windows fallback
    
    # Tạo bản copy để render
    display_map = [row[:] for row in MAP]
    
    # Đặt toà thị chính
    th_x, th_y = TOWN_HALL_POS
    if 0 <= th_y < len(display_map) and 0 <= th_x < len(display_map[0]):
        display_map[th_y][th_x] = TILE_TOWN_HALL
    
    # Đặt người chơi
    if 0 <= player_y < len(display_map) and 0 <= player_x < len(display_map[0]):
        display_map[player_y][player_x] = "@"
    
    # Render ra emoji
    for row in display_map:
        line = ""
        for cell in row:
            if cell == "@":
                line += "@"
            else:
                line += TILE_DISPLAY.get(cell, "?")
        print(line)


def get_tile(x, y):
    """Lấy loại tile ở vị trí (x, y)."""
    if 0 <= y < len(MAP) and 0 <= x < len(MAP[0]):
        return MAP[y][x]
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