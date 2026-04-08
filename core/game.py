"""
Country Box - engine chính.
- Lưu state game vào dictionary.
- Để bạn dễ nâng cấp bằng comment tiếng Việt.
- Giữ code ngắn gọn, tách rõ chức năng.
"""

from core import commands
from core import map_render


# tạo villager mặc định
# mỗi villager có name, hunger, thirst, status
def new_villager(index):
    return {
        "name": f"villager{index + 1}",
        "hunger": 50,
        "thirst": 50,
        "status": "idle",
    }


# tạo game mới
def new_game():
    return {
        "turn": 1,
        "player": {"x": 2, "y": 2},
        "inventory": {
            "food": 10,
            "water": 10,
            "wood": 0,
            "stone": 0,
            "axe": 0,
            "pickaxe": 0,
        },
        "villagers": [new_villager(i) for i in range(10)],
        "messages": [],
    }


# thêm message vào game log
def add_message(game, text):
    game["messages"].append(text)


# báo cáo trạng thái game
def status_report(game):
    inventory = game["inventory"]
    report = [
        f"Turn: {game['turn']}",
        f"Food: {inventory['food']} | Water: {inventory['water']} | Wood: {inventory['wood']} | Stone: {inventory['stone']}",
        f"Axe: {inventory['axe']} | Pickaxe: {inventory['pickaxe']}",
        "Villagers:",
    ]
    for v in game["villagers"]:
        report.append(f"  - {v['name']}: hunger={v['hunger']} thirst={v['thirst']} status={v['status']}")
    return "\n".join(report)


# trừ nguyên liệu khi chế tạo
def spend_resources(game, cost):
    for key, amount in cost.items():
        if game["inventory"].get(key, 0) < amount:
            return False
    for key, amount in cost.items():
        game["inventory"][key] -= amount
    return True


# lệnh hey_village find *
def command_find(game, item):
    if item not in ["wood", "stone", "food", "water"]:
        add_message(game, f"Không biết tìm {item}. Hãy thử wood, stone, food hoặc water.")
        return

    if item in ["wood", "stone", "food"]:
        result = map_render.harvest_tile(game["player"]["x"], game["player"]["y"])
        if result == item:
            game["inventory"][item] += 1
            add_message(game, f"Thu thập được 1 {item} từ ô hiện tại.")
        elif result is None:
            add_message(game, f"Không tìm thấy {item} ở ô này. Dân làng vẫn cố gắng, nhưng không mang được gì.")
        else:
            game["inventory"][result] += 1
            add_message(game, f"Dân làng thu thập được 1 {result} thay vì {item}.")
    elif item == "water":
        game["inventory"]["water"] += 1
        add_message(game, "Dân làng đã lấy được 1 nước.")


# lệnh hey_village make *
def command_make(game, item):
    recipes = {
        "axe": {"wood": 2},
        "pickaxe": {"wood": 2, "stone": 2},
        "food": {"food": 1, "water": 1},
    }
    if item not in recipes:
        add_message(game, f"Không thể chế tạo {item}. Thử axe, pickaxe hoặc food.")
        return

    if spend_resources(game, recipes[item]):
        if item == "food":
            game["inventory"]["food"] += 2
            add_message(game, "Chế biến thành công 2 food.")
        else:
            game["inventory"][item] += 1
            add_message(game, f"Chế tạo thành công 1 {item}.")
    else:
        add_message(game, "Không đủ nguyên liệu để chế tạo.")


# cập nhật mỗi lượt
def turn_tick(game):
    game["turn"] += 1
    for v in game["villagers"]:
        v["hunger"] = max(0, v["hunger"] - 5)
        v["thirst"] = max(0, v["thirst"] - 5)
        if v["hunger"] < 20 or v["thirst"] < 20:
            v["status"] = "hungry"
        else:
            v["status"] = "idle"

    # nếu dân đói hoặc khát thì tự động ăn/uống nếu còn trong kho
    for v in game["villagers"]:
        if v["hunger"] < 20 and game["inventory"]["food"] > 0:
            game["inventory"]["food"] -= 1
            v["hunger"] = min(100, v["hunger"] + 25)
            add_message(game, f"{v['name']} đã ăn để giữ sức.")
            break
        if v["thirst"] < 20 and game["inventory"]["water"] > 0:
            game["inventory"]["water"] -= 1
            v["thirst"] = min(100, v["thirst"] + 25)
            add_message(game, f"{v['name']} đã uống nước.")
            break


# xử lý lệnh người chơi
def process_command(game, text):
    action, args = commands.parse_command(text)
    if action == "find":
        command_find(game, args[0])
    elif action == "make":
        command_make(game, args[0])
    elif action == "status":
        add_message(game, status_report(game))
    elif action == "move":
        dx, dy = args
        new_x = game["player"]["x"] + dx
        new_y = game["player"]["y"] + dy
        if map_render.is_walkable(new_x, new_y):
            game["player"]["x"] = new_x
            game["player"]["y"] = new_y
            add_message(game, f"Di chuyển đến ({new_x}, {new_y}).")
        else:
            add_message(game, "Không thể đi tới ô đó.")
    elif action == "help":
        add_message(game, commands.command_help())
    else:
        add_message(game, "Lệnh không hợp lệ. Gõ help để xem lệnh.")

    turn_tick(game)


# in message + map + status sau mỗi lượt
def show(game):
    print("\n".join(game["messages"]))
    game["messages"].clear()
    print("\nBản đồ hiện tại:")
    map_render.render(game["player"]["x"], game["player"]["y"])
    print("\n" + status_report(game))


# khởi động game
def main():
    game = new_game()
    add_message(game, "Chào mừng đến Country Box! Gõ help để bắt đầu.")
    while True:
        show(game)
        command = input("> ").strip()
        if command in ["exit", "quit"]:
            print("Tạm biệt!")
            break
        process_command(game, command)


if __name__ == "__main__":
    main()
