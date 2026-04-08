-- villager
-- noi ma logic cua dan lang se o day
-- day la mob tach va kha nang se ap dung cho open mod 

-- version: 1.0 
-- tao ra boi Khoapython-dev

-- data se duoc chuyen tu python engine sang
-- nen ban se khong the nhin thay

-- kiem tra sinh ton def
function check_survival()
  if hunger < 10 then
    return "villager will die if storage don't have food!"
  elseif thirst < 10 then
    return "villager is thirsting!"
  end 
end
-- nhin duong
function check_road()
  if AHEAD_IS_STONE == true then
    -- kiem tra do dung 
    if PICKAXE == 0 then
      return "can't mine without pickaxe!"
    else then
      return {"inventory": {"stone": 1}, "pickaxe": -2}
    end 
  elseif AHEAD_IS_WOOD == true then
    if AXE > 0 then  
      return {"inventory": {"wood": 1}, "axe": -2}
    elseif AXE < 0 then
      return {"inventory": {"wood": 1}}
    end
  
  elseif AHEAD_IS_NONE then
    return "Nothing"
  
-- tuy chon: auto random di chuyeb
function move(startstep, endstep)
  return math.random(startstep, endstep)

  
  
      
    
    
    