-- villager.lua
-- logic của dân làng cho Country Box v1.4
-- hỗ trợ tự động khai thác, lấy nước, sử dụng trang bị
-- version: 1.4
-- tạo bởi Khoapython-dev

-- data từ Python engine
-- hunger, thirst, inventory, durability, etc.

-- kiểm tra sinh tồn
function check_survival()
  if hunger < 10 then
    return "villager will die if storage don't have food!"
  elseif thirst < 10 then
    return "villager is thirsting!"
  end
end

-- kiểm tra đường phía trước
function check_road()
  if AHEAD_IS_STONE == true then
    -- kiểm tra độ bền cúp
    if PICKAXE_STONE > 0 then
      return {"inventory": {"stone": 1}, "durability": {"pickaxe_stone": -2}}
    elseif PICKAXE_WOOD > 0 then
      return {"inventory": {"stone": 1}, "durability": {"pickaxe_wood": -5}}
    else
      return "can't mine without pickaxe!"
    end
  elseif AHEAD_IS_WOOD == true then
    if AXE_STONE > 0 then
      return {"inventory": {"wood": 1}, "durability": {"axe_stone": -2}}
    elseif AXE_WOOD > 0 then
      return {"inventory": {"wood": 1}, "durability": {"axe_wood": -5}}
    else
      return {"inventory": {"wood": 1}}  -- chặt tay không
    end
  elseif AHEAD_IS_RIVER == true then
    return {"inventory": {"water": 1}}
  elseif AHEAD_IS_NONE then
    return "Nothing"
  end
end

-- tự động di chuyển ngẫu nhiên
function move(startstep, endstep)
  return math.random(startstep, endstep)
end

-- logic tự động hành động mỗi lượt
function auto_action()
  -- nếu đói, tìm thức ăn
  if hunger < 20 and FOOD_STORAGE > 0 then
    return {"consume": {"food": 1}, "hunger": +25}
  end
  -- nếu khát, tìm nước gần đó
  if thirst < 20 then
    if NEARBY_RIVER then
      return {"inventory": {"water": 1}, "thirst": +25}
    elseif WATER_STORAGE > 0 then
      return {"consume": {"water": 1}, "thirst": +25}
    end
  end
  -- nếu rảnh, di chuyển ngẫu nhiên để tìm tài nguyên
  return {"move": move(-1, 1), "move": move(-1, 1)}
end

  
  
      
    
    
    