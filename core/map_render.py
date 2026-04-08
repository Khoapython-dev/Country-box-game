"""
map render va su dung de di chuyen trong map
- su dung nhung nhan vat, dan lang se di chuyen va render len map
- # la tuong
- | la cay
- ∆ la da 
- . la duong di/dat 
- % thuc an
made by Khoapython-dev
1.0
"""
MAP = {
  list("####################") # that ra map la 20x18
  list("#..................#")
  list("#...|........%.....#")
  list("#.......∆..........#")
  list("#..................#")
  list("#.............|....#")
  list("#....∆.............#")
  list("#......|...........#")
  list("#.............∆....#")
  list("#........∆∆........#")
  list("#..................#")
  list("#...........|..%...#")
  list("#..................#")
  list("#...%..............#")
  list("#...............∆..#")
  list("#.....|............#")
  list("#..................#")
  list("#.......∆..........#")
  list("####################")
}
def render():
  print(MAP)
  
def move(x, y, character_theme):
  try:
    if MAP[x] == "#" and MAP[y] == "#":
      return "0b00382::wall"
    elif MAP[x] == "|" and MAP[y] == "|":
      return "0b00583::wood"
    elif MAP[x] == "∆" and MAP[y] == "∆":
      return "0b00692::stone"
    elif MAP[x] == "%" and MAP[y] == "%":
    MAP[x][y] = character_theme
  