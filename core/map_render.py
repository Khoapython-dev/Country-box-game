"""
map render và logic đơn giản cho Country Box.
- Bản đồ nhỏ để dễ debug.
- Cấm đi xuyên tường.
- Thu thập tài nguyên bằng harvest.
- Phù hợp cho mô hình terminal game.
"""

MAP = [
    list("#####"),
    list("#...#"),
    list("#.@.#"),
    list("#.%.#"),
    list("#####"),
]


# render map mỗi lượt
# @ là vị trí người chơi hiện tại
def render(player_x, player_y):
    render_map = [row.copy() for row in MAP]
    if 0 <= player_y < len(render_map) and 0 <= player_x < len(render_map[0]):
        render_map[player_y][player_x] = "@"
    for row in render_map:
        print("".join(row))


# lấy ký tự ô map
def get_tile(x, y):
    if 0 <= y < len(MAP) and 0 <= x < len(MAP[0]):
        return MAP[y][x]
    return "#"


# kiểm tra ô có thể đi vào không
def is_walkable(x, y):
    tile = get_tile(x, y)
    return tile in [".", "%", "|", "∆", "@"]


# thu thập tài nguyên ở ô hiện tại
# nếu đúng loại thì đổi ô thành đường đi
def harvest_tile(x, y):
    tile = get_tile(x, y)
    if tile == "%":
        MAP[y][x] = "."
        return "food"
    if tile == "|":
        MAP[y][x] = "."
        return "wood"
    if tile == "∆":
        MAP[y][x] = "."
        return "stone"
    return None
  