-- entities/chicken.lua
-- Logic cho con gà trong game
-- Gà sẽ di chuyển ngẫu nhiên xung quanh map
-- Nếu gặp dân làng có thể bị giết

-- chicken state: {x, y, hunger, alive}
-- khi alive=false, gà đã bị giết, sẽ bị xóa khỏi map

function new_chicken(x, y)
  return {
    x = x,
    y = y,
    id = math.random(1000000),
    hunger = 50,
    alive = true,
    last_move = 0,
  }
end

-- AI: di chuyển ngẫu nhiên
function move_random(chicken, map_width, map_height)
  if not chicken.alive then
    return chicken
  end
  
  -- di chuyển sau mỗi 2 lượt
  chicken.last_move = chicken.last_move + 1
  if chicken.last_move < 2 then
    return chicken
  end
  chicken.last_move = 0
  
  -- chọn hướng ngẫu nhiên: up, down, left, right
  local directions = {
    {0, -1},  -- up
    {0, 1},   -- down
    {-1, 0},  -- left
    {1, 0},   -- right
  }
  local dir = directions[math.random(1, 4)]
  local new_x = chicken.x + dir[1]
  local new_y = chicken.y + dir[2]
  
  -- check bounds
  if new_x >= 0 and new_x < map_width and new_y >= 0 and new_y < map_height then
    chicken.x = new_x
    chicken.y = new_y
  end
  
  -- độ đói tăng mỗi lượt
  chicken.hunger = math.max(0, chicken.hunger - 2)
  
  return chicken
end

-- nếu gặp dân làng, gà có 50% chance bị giết
function check_collision_with_villager(chicken, villager)
  if not chicken.alive then
    return false, 0
  end
  
  local distance = math.sqrt((chicken.x - villager.x) ^ 2 + (chicken.y - villager.y) ^ 2)
  if distance < 2 then  -- gần dân làng
    if math.random() < 0.5 then
      chicken.alive = false
      return true, math.random(2, 3)  -- giết gà, nhận 2-3 food
    end
  end
  
  return false, 0
end

-- return hiện tại của gà cho Python render
function serialize(chicken)
  return {
    x = chicken.x,
    y = chicken.y,
    id = chicken.id,
    alive = chicken.alive,
    hunger = chicken.hunger,
  }
end
