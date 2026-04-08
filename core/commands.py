"""
Parser cho lệnh CLI của Country Box.
- Nhận lệnh từ user.
- Trả về action + args để engine xử lý.
- Đơn giản, dễ đọc, dễ sửa.
"""


def parse_command(text):
    text = text.strip()
    # hey_village find * wood
    if text.startswith("hey_village find "):
        rest = text[16:].strip()
        if rest.startswith("*"):
            rest = rest[1:].strip()
        return ("find", [rest])
    # hey_village make * axe
    if text.startswith("hey_village make "):
        rest = text[16:].strip()
        if rest.startswith("*"):
            rest = rest[1:].strip()
        return ("make", [rest])
    # kiểm tra trạng thái đói khát
    if text == "hey_village are_you_hungry?":
        return ("status", [])
    # di chuyển trên map
    if text.startswith("hey_village move "):
        parts = text.split()
        if len(parts) == 4:
            try:
                dx = int(parts[2])
                dy = int(parts[3])
                return ("move", [dx, dy])
            except ValueError:
                return ("unknown", [text])
    if text == "help":
        return ("help", [])
    return ("unknown", [text])


def command_help():
    return """
Các lệnh hiện có:
  hey_village find * [wood|stone|food|water]
  hey_village make * [axe_wood|axe_stone|pickaxe_wood|pickaxe_stone|food]
  hey_village are_you_hungry?
  hey_village move dx dy     # dx, dy là số nguyên, tự động khai thác
  help
  quit / exit
""".strip()
