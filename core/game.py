"""
Country Box - engine chính.
- Lưu state game vào dictionary.
- Để bạn dễ nâng cấp bằng comment tiếng Việt.
- Giữ code ngắn gọn, tách rõ chức năng.
- v1.7.8: Tích hợp entities (gà) từ entity_manager
"""

import random

from core import commands
from core import map_render
from core.entity_manager import EntityManager

ROLE_LABELS = {
    "miner": "⛏️ Thợ mỏ",
    "lumberjack": "🪓 Tiều phu",
    "cook": "🍳 Đầu bếp",
    "guard": "🛡️ Lính canh",
}

WEATHER_LABELS = {
    "sunny": "☀️ Nắng",
    "rain": "🌧️ Mưa",
    "snow": "❄️ Băng giá",
}


# tạo villager mặc định
# mỗi villager có name, hunger, thirst, status, role
def new_villager(index):
    roles = ["miner", "lumberjack", "cook", "guard"]
    role = roles[index % len(roles)]
    return {
        "name": f"villager{index + 1}",
        "role": role,
        "hunger": 50,
        "thirst": 50,
        "status": "idle",
        "x": 10,  # vị trí toà thị chính
        "y": 9,
    }


def new_game():
    game = {
        "turn": 1,
        "hour": 6,
        "weather": "sunny",
        "weather_duration": 5,
        "next_threat_turn": 12,
        "player": {"x": 10, "y": 9},  # vị trí toà thị chính
        "inventory": {
            "food": 15,
            "water": 15,
            "wood": 30,
            "stone": 30,
            "iron": 0,
            "steel": 0,
            "axe_wood": 0,
            "axe_stone": 0,
            "axe_steel": 0,
            "pickaxe_wood": 0,
            "pickaxe_stone": 0,
            "pickaxe_steel": 0,
        },
        "durability": {
            "axe_wood": 75,
            "axe_stone": 100,
            "axe_steel": 150,
            "pickaxe_wood": 75,
            "pickaxe_stone": 100,
            "pickaxe_steel": 150,
        },
        "villagers": [new_villager(i) for i in range(10)],
        "structures": {"smelter": False},
        "messages": [],
        "entity_manager": EntityManager(),  # v1.7.8: Quản lý entities (gà)
    }
    # spawn gà xung quanh map
    game["entity_manager"].spawn_chickens(count=8, map_width=20, map_height=18)
    return game


def get_time_of_day(hour):
    return "day" if 6 <= hour < 18 else "night"


def format_hour(hour):
    return f"{hour:02d}:00"


def choose_new_weather(game):
    game["weather"] = random.choice(["sunny", "rain", "snow"])
    game["weather_duration"] = random.randint(4, 7)
    add_message(game, f"Thời tiết đổi sang {WEATHER_LABELS[game['weather']]}.")


def get_role_harvest_extra(game, item):
    mapping = {
        "wood": "lumberjack",
        "stone": "miner",
        "food": "cook",
        "water": "cook",
    }
    role = mapping.get(item)
    if not role:
        return 0
    count = sum(1 for v in game["villagers"] if v["role"] == role)
    return min(count, 2)


def is_night(game):
    return get_time_of_day(game["hour"]) == "night"


def get_guard_count(game):
    return sum(1 for v in game["villagers"] if v["role"] == "guard")


def add_message(game, text):
    game["messages"].append(text)


def status_report(game):
    inventory = game["inventory"]
    durability = game.get("durability", {})
    report = [
        f"Turn: {game['turn']} ({format_hour(game['hour'])} - {get_time_of_day(game['hour'])})",
        f"Weather: {WEATHER_LABELS.get(game['weather'], game['weather'])}",
        f"Food: {inventory['food']} | Water: {inventory['water']} | Wood: {inventory['wood']} | Stone: {inventory['stone']} | Iron: {inventory['iron']} | Steel: {inventory['steel']}",
        f"Axe Wood: {inventory['axe_wood']} (dur: {durability.get('axe_wood', 0)}) | Axe Stone: {inventory['axe_stone']} (dur: {durability.get('axe_stone', 0)}) | Axe Steel: {inventory['axe_steel']} (dur: {durability.get('axe_steel', 0)})",
        f"Pickaxe Wood: {inventory['pickaxe_wood']} (dur: {durability.get('pickaxe_wood', 0)}) | Pickaxe Stone: {inventory['pickaxe_stone']} (dur: {durability.get('pickaxe_stone', 0)}) | Pickaxe Steel: {inventory['pickaxe_steel']} (dur: {durability.get('pickaxe_steel', 0)})",
        f"Smelter: {'✅ Đã xây' if game['structures'].get('smelter') else '❌ Chưa xây'}",
        "Villagers:",
    ]
    for v in game["villagers"]:
        role_label = ROLE_LABELS.get(v["role"], v["role"])
        report.append(f"  - {v['name']} ({role_label}): hunger={v['hunger']} thirst={v['thirst']} status={v['status']}")
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
        if is_night(game) and random.random() < 0.30:
            add_message(game, "Ban đêm, dân làng khai thác chậm và không thu được gì.")
            return

        result = map_render.harvest_tile(game["player"]["x"], game["player"]["y"])
        if result == item:
            extra = get_role_harvest_extra(game, item)
            gained = 1 + extra
            game["inventory"][item] += gained
            if extra:
                add_message(game, f"Thu thập được {gained} {item} từ ô hiện tại (vai trò hỗ trợ +{extra}).")
            else:
                add_message(game, f"Thu thập được 1 {item} từ ô hiện tại.")
        elif result is None:
            add_message(game, f"Không tìm thấy {item} ở ô này. Dân làng vẫn cố gắng, nhưng không mang được gì.")
        else:
            extra = get_role_harvest_extra(game, result)
            gained = 1 + extra if result != "water" else 1
            game["inventory"][result] += gained
            add_message(game, f"Dân làng thu thập được {gained} {result} thay vì {item}.")
    elif item == "water":
        game["inventory"]["water"] += 1
        add_message(game, "Dân làng đã lấy được 1 nước.")


def command_make(game, item):
    aliases = {
        "axe": "axe_wood",
        "wood_axe": "axe_wood",
        "stone_axe": "axe_stone",
        "pickaxe": "pickaxe_wood",
        "wood_pickaxe": "pickaxe_wood",
        "stone_pickaxe": "pickaxe_stone",
    }
    item = aliases.get(item, item)

    recipes = {
        "smelter": {"wood": 10, "stone": 10},
        "iron": {"stone": 4},
        "steel": {"iron": 2, "stone": 2},
        "axe_wood": {"wood": 3},
        "axe_stone": {"wood": 1, "stone": 2},
        "axe_steel": {"wood": 1, "iron": 1, "steel": 1},
        "pickaxe_wood": {"wood": 3},
        "pickaxe_stone": {"wood": 1, "stone": 2},
        "pickaxe_steel": {"wood": 1, "iron": 1, "steel": 1},
        "food": {"food": 1, "water": 1},
    }

    if item not in recipes:
        add_message(game, f"Không thể chế tạo {item}. Thử smelter, iron, steel, axe_wood, axe_stone, axe_steel, pickaxe_wood, pickaxe_stone, pickaxe_steel hoặc food.")
        return

    if item in ["iron", "steel"] and not game["structures"].get("smelter"):
        add_message(game, "Cần xây smelter trước khi luyện iron hoặc steel.")
        return

    if item == "smelter":
        if spend_resources(game, recipes[item]):
            game["structures"]["smelter"] = True
            add_message(game, "Đã xây xong smelter. Bạn có thể luyện iron và steel.")
        else:
            add_message(game, "Không đủ nguyên liệu để xây smelter.")
        return

    if spend_resources(game, recipes[item]):
        if item == "food":
            game["inventory"]["food"] += 2
            add_message(game, "Chế biến thành công 2 food.")
        elif item in ["iron", "steel"]:
            game["inventory"][item] += 1
            add_message(game, f"Luyện thành công 1 {item}.")
        else:
            game["inventory"][item] += 1
            if item in ["axe_stone", "pickaxe_stone"]:
                game["durability"][item] += 25
            elif item in ["axe_wood", "pickaxe_wood"]:
                game["durability"][item] += 15
            elif item in ["axe_steel", "pickaxe_steel"]:
                game["durability"][item] += 50
            add_message(game, f"Chế tạo thành công 1 {item}.")
    else:
        add_message(game, "Không đủ nguyên liệu để chế tạo.")


# cập nhật mỗi lượt
def turn_tick(game):
    game["turn"] += 1
    game["hour"] = (game["hour"] + 1) % 24
    game["weather_duration"] -= 1
    if game["weather_duration"] <= 0:
        choose_new_weather(game)

    if game["weather"] == "rain" and random.random() < 0.35:
        game["inventory"]["water"] += 1
        add_message(game, "🌧️ Mưa giúp thu được 1 nước tự động.")
    if game["weather"] == "snow":
        for v in game["villagers"]:
            v["hunger"] = max(0, v["hunger"] - 1)
        if game["turn"] % 3 == 0:
            add_message(game, "❄️ Băng giá khiến dân làng lạnh lùng và đói hơn.")

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

    if game["turn"] >= game["next_threat_turn"]:
        threat = random.choice(["wolf", "bandit"])
        guard_count = get_guard_count(game)
        defense = 0.35 + 0.15 * guard_count
        threat_name = "🐺 Sói" if threat == "wolf" else "👹 Bandit"
        if guard_count > 0 and random.random() < defense:
            add_message(game, f"{threat_name} tấn công, nhưng lính canh đã chặn được.")
        else:
            if guard_count == 0 and game["villagers"]:
                victim = random.choice(game["villagers"])
                game["villagers"].remove(victim)
                add_message(game, f"{threat_name} đã giết {victim['name']} do không có lính canh.")
            else:
                loss_item = random.choice(["food", "wood", "stone"])
                loss_amount = min(game["inventory"][loss_item], random.randint(1, 3))
                game["inventory"][loss_item] -= loss_amount
                add_message(game, f"{threat_name} làm mất {loss_amount} {loss_item} dù có lính canh.")
        game["next_threat_turn"] = game["turn"] + random.randint(10, 15)

    # v1.7.8: cập nhật entities (gà, v.v)
    result = game["entity_manager"].update(
        map_width=20,
        map_height=18,
        villagers=game["villagers"]
    )
    # xử lý gà bị giết - thêm thực phẩm vào kho
    killed_chickens = result.get("killed_chickens", [])
    if killed_chickens:
        total_food = sum(food for x, y, food in killed_chickens)
        game["inventory"]["food"] += total_food
        add_message(game, f"🐔 Gà bị giết, sản phẩm: +{total_food} thức ăn từ {len(killed_chickens)} con gà.")


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
            harvested = map_render.harvest_tile(new_x, new_y)
            if harvested:
                if is_night(game) and random.random() < 0.30:
                    add_message(game, "Ban đêm, dân làng khai thác chậm và không thu được gì.")
                else:
                    extra = get_role_harvest_extra(game, harvested)
                    gained = 1 + extra
                    game["inventory"][harvested] += gained
                    if extra:
                        add_message(game, f"Dân làng tự động khai thác được {gained} {harvested} (vai trò hỗ trợ +{extra}).")
                    else:
                        add_message(game, f"Dân làng tự động khai thác được 1 {harvested}.")
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
    
    # v1.7.8: hiển thị thông tin entities
    chickens = game["entity_manager"].get_all_positions()
    if chickens:
        print(f"🐔 Gà trên bản đồ: {len(chickens)} con")
        for i, (x, y) in enumerate(chickens[:5]):  # hiển thị 5 con đầu tiên
            print(f"  Gà {i+1}: ({x}, {y})")
        if len(chickens) > 5:
            print(f"  ... và {len(chickens) - 5} con khác")
    
    print("\n" + status_report(game))


def main():
    game = new_game()
    add_message(game, "Chào mừng đến Country Box v1.4! Gõ help để bắt đầu.")
    while True:
        show(game)
        command = input("> ").strip()
        if command in ["exit", "quit"]:
            print("Tạm biệt!")
            break
        process_command(game, command)


if __name__ == "__main__":
    main()
