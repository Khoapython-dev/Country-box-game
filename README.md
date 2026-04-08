# 📦 COUNTRY BOX

> *Xây làng. Nuôi dân. Sinh tồn.*

Country Box là một game mô phỏng làng xã chạy trên terminal. Bạn điều khiển để dân làng thu thập tài nguyên, chế tạo, xây dựng và giữ cho cả làng sống sót.

---

## 🎮 Cách chơi

Ban đầu bạn có:
- 👥 **10 dân làng**
- 🍖 **15 thức ăn** | 💧 **15 nước**
- 🪵 **30 gỗ** | 🪨 **30 đá**
- 🏰 **Toà thị chính** tại vị trí trung tâm map

Mỗi lượt bạn nhập lệnh và hệ thống game sẽ tiến 1 lượt:
- Độ đói và độ khát của dân làng giảm.
- Dân làng có thể tự động ăn/uống nếu thiếu.
- Dân làng tự động khai thác khi di chuyển vào ô có tài nguyên.

---

## 💻 Lệnh điều khiển

```bash
# Yêu cầu dân làng đi thu thập tài nguyên trên ô hiện tại
hey_village find * [wood|stone|food|water]

# Yêu cầu dân làng chế tạo hoặc xây
hey_village make * [smelter|iron|steel|axe_wood|axe_stone|axe_steel|pickaxe_wood|pickaxe_stone|pickaxe_steel|food]

# Kiểm tra tình trạng dân làng
hey_village are_you_hungry?

# Di chuyển và tự động khai thác nếu có tài nguyên
hey_village move dx dy

# Xem trợ giúp và thoát
help
quit / exit
```

---

## 🌍 Bản đồ và hiển thị

Map hiện tại có kích thước **20x18** với các ký hiệu:
- `@` = người chơi
- `🏰` = toà thị chính
- `🌲` = gỗ
- `🪨` = đá
- `⛰️` = núi đá (không thể đi qua)
- `🏞️` = sông (lấy nước)
- `#` = tường không qua được

---

## ⭐️ Tính năng hiện tại

- Role system cho dân làng:
  - `⛏️ Thợ mỏ`
  - `🪓 Tiều phu`
  - `🍳 Đầu bếp`
  - `🛡️ Lính canh`
- Chu kỳ **ngày/đêm** với hiệu suất khai thác khác nhau.
- Hệ thống **thời tiết**: `☀️ Nắng`, `🌧️ Mưa`, `❄️ Băng giá`.
- **Threat system**: `🐺 Sói` hoặc `👹 Bandit` tấn công sau một số lượt.
- **Tech tree** cơ bản:
  - Xây `smelter`
  - Luyện `iron`
  - Luyện `steel`
  - Chế tạo `axe_steel` và `pickaxe_steel`
- Dân làng tự động ăn/uống khi thiếu.
- Hệ thống **inventory**: food, water, wood, stone, iron, steel.

---

## 🧠 Mục tiêu

Giữ cho dân làng sống sót và phát triển lâu dài bằng cách cân bằng:
- Ăn uống
- Tài nguyên
- Công cụ và cấu trúc
- Threat và phòng thủ

---

## 🚀 Khởi động game

Chạy từ thư mục gốc:

```bash
cd /workspaces/Country-box-game
python3 -m core.game
```

Hoặc:

```bash
python3 core/game.py
```

---

## 📜 Lịch sử cập nhật

v1.8.0 by Khoapython-dev:
- Thêm hệ thống vai trò dân làng: ⛏️ Thợ mỏ, 🪓 Tiều phu, 🍳 Đầu bếp, 🛡️ Lính canh.
- Thêm chu kỳ ngày/đêm.
- Thêm thời tiết: ☀️ Nắng, 🌧️ Mưa, ❄️ Băng giá.
- Thêm threat system: 🐺 Sói và 👹 Bandit.
- Thêm tech tree: `smelter`, `iron`, `steel`, `axe_steel`, `pickaxe_steel`.

v1.7.9 by Alex-claudevibe

v1.7.8 (transfer version) by Khoapython-dev:
- Hiển thị và logic entities gà.
- Mở rộng map, warehouse, entity system.
- Hệ thống mod logic.

v1.4.1 (1.3.7 catch) by Khoapython-dev:
- Alias chế tạo.
- Tăng tài nguyên khởi đầu.
- Đề xuất lưu recipe và save game.

v1.4 (1.3.6 Beta) by Khoapython-dev:
- Bản đồ 20x18.
- Hệ thống cơ bản: food, water, wood, stone.
- Trang bị rìu/cúp.
- Dân làng tự động khai thác và ăn/uống.

---

## 📝 Ghi chú

Nếu bạn muốn mở rộng tiếp, có thể thêm ngay:
- Event system JSON
- Population system
- Diplomacy / multi-village
- Save/load game
# 📦 COUNTRY BOX

> *Xây làng. Nuôi dân. Sinh tồn.*

Một tựa game mô phỏng làng xã chạy trên terminal — bạn ra lệnh cho 10 dân làng
thu thập tài nguyên, chế tạo đồ, và phát triển khu định cư của mình.

---

## 🎮 Cách chơi

Bạn bắt đầu với:
- 👥 **10 dân làng** sẵn sàng làm việc
- 🍖 **15 thức ăn** | 💧 **15 nước uống** | 🪵 **30 gỗ** | 🪨 **30 đá**
- 🗺️ Bản đồ **20x18** để khám phá và xây dựng

Dân làng có thể tự suy nghĩ — nếu đói mà bạn không để ý,
chúng sẽ tự đi săn. Hãy giữ cho chúng no và còn sống!

---

## 💻 Lệnh điều khiển

```bash
# Yêu cầu dân làng đi thu thập tài nguyên trên ô hiện tại
hey_village find * [wood|stone|food|water]

# Yêu cầu dân làng chế tạo hoặc xây
hey_village make * [smelter|iron|steel|axe_wood|axe_stone|axe_steel|pickaxe_wood|pickaxe_stone|pickaxe_steel|food]

# Kiểm tra tình trạng dân làng
hey_village are_you_hungry?

# Di chuyển và tự động khai thác nếu có tài nguyên
hey_village move dx dy

# Xem trợ giúp và thoát
help
quit / exit
```

🔄 Hệ thống lượt
- Mỗi lệnh = 1 lượt.
- Mỗi lượt: 🍖 độ đói & 💧 độ khát giảm.
- Dân làng rảnh có thể tự động ăn/uống.
- Di chuyển đến ô có tài nguyên sẽ tự động khai thác.

🗺️ Bản đồ hiện tại
- Sử dụng emoji:
  - "🏰" toà thị chính
  - "🌲" cây
  - "🪨" đá
  - "⛰️" núi đá (không đi qua được)
  - "🏞️" sông (lấy nước)
  - "#" tường không đi qua

📋 Lịch sử cập nhật
Phiên bản
Ghi chú (nếu có ý tưởng, hãy bổ sung và ghi tên mình vào)

v1.7.9 by Alex-claudevibe
v1.8.0 by Khoapython-dev:
- Thêm hệ thống vai trò dân làng: ⛏️ Thợ mỏ, 🪓 Tiều phu, 🍳 Đầu bếp, 🛡️ Lính canh.
- Thêm chu kỳ ngày/đêm: ban đêm hiệu suất khai thác giảm, game hiển thị giờ trong status.
- Thêm thời tiết: ☀️ Nắng, 🌧️ Mưa, ❄️ Băng. Mưa tự động thu nước, băng làm dân làng đói nhanh hơn.
- Thêm threat system: 🐺 Sói và 👹 Bandit sẽ tấn công sau một số lượt, cần có Guard để chặn.
- Thêm tech tree đơn giản: xây smelter rồi luyện iron và steel, có thêm axe_steel và pickaxe_steel.

v1.7.8 (transfer version) by Khoapython-dev:
* hiển thị:
- chuyển sang dùng textual lib
- dân làng sẽ chạy ngẫu nhiên đến 1 ô nào đó, nếu xung quanh là 1 vật phẩm khai thác được, dân làng sẽ khai thác=> texture biến mất trên map)
- mở rộng map từ 20x18 lên 95x75
- spam ngẫu nhiên toàn bộ vật phẩm trên map (nhiều hơn cho phép dân làng có nhiều vật phẩm hơn)
- bổ sung công trình mới: 🛖 nhà kho (công sức chứa toàn bộ vật phẩm là 200) (spam ngẫu nhiên xung quanh nhà chính 3 - 4 block)
- bổ sung động vật: 🐔 Gà
gà sẽ spam và đi xung quanh, dân làng nếu bắt gặp có thể giết nó và có thức ăn (+2 ~ +3) (logic ở chicken.lua)
- bổ sung main menu

* logic:
- mở rộng mod (dành cho logic của game ở mods/private/..mod) có thể mở rộng logic ở đây nhé thay vì sử dụng mỗi python 
- sau khi tất cả dân làng đều chết, hiện: lose, quốc gia của bạn đã chết 
[END] nếu có ý tưởng? tiếp tục điền ở đây:



v1.4.1 (1.3.7 catch) by Khoapython-dev:
- Cập nhật README để ghi rõ map 20x18 và lệnh hiện tại.
- Thêm alias cho chế tạo: `axe`, `pickaxe`, `wood_pickaxe`, `stone_pickaxe`, `wood_axe`, `stone_axe`.
- Hiện tại vẫn là ý tưởng để mở rộng:
  - lưu công thức chế tạo vào `data/recipe.json`.
  - lưu tiến trình vào `saves/world-<timestamp>.json`.
  - AI tự động tìm tài nguyên theo loại chứ không chỉ ô hiện tại.
  - thêm chỉ thị `🧍` cho mỗi dân làng và biểu tượng đồ ăn `🍎🍌🥦`.

v1.4 (1.3.6 Beta) by Khoapython-dev:
- Nâng cấp bản đồ lên 20x18.
- Các thiết yếu ban đầu:
  + nước: 15, thức ăn: 15
  + gỗ: 30
  + đá: 30

- Trang bị:
  + cúp đá (độ bền) 100
  + cúp gỗ: 75
  + rìu đá: 100
  + rìu gỗ: 75

- Công thức mới:
  + 2 đá + 1 gỗ -> cúp/rìu đá (độ bền +25)
  + 3 gỗ -> cúp/rìu gỗ (độ bền +15)

- Dân làng tự động khai thác tài nguyên bằng cách di chuyển đến ô có tài nguyên.
- Dân làng tự động ăn và uống khi cần.
- Dùng emoji thay vì ASCII.
- Dùng `clear` để làm mới màn hình.
- Logic dân làng tiếp tục được mở rộng trong `villager.lua`.

v1.3
Phát hành lần đầu 🎉
v1.1
Bản nội bộ
🔮 Tính năng sắp ra
[ ] 🧍 Tên & tính cách riêng cho từng dân làng
[ ] ⚔️ Hệ thống mối đe dọa & phòng thủ
[ ] 🏗️ Xây dựng công trình
[ ] 🌦️ Thời tiết & mùa vụ
[ ] 🧩 Hỗ trợ mod (nhân vật, vật phẩm, sự kiện)
👾 Làm bằng tình yêu (và quá nhiều giờ trong terminal)
CLI 1.3 — Phiên bản đầu tiên. Hy vọng các bạn thích! =))
---

v1.3
Phát hành lần đầu 🎉
v1.1
Bản nội bộ
🔮 Tính năng sắp ra
[ ] 🧍 Tên & tính cách riêng cho từng dân làng
[ ] ⚔️ Hệ thống mối đe dọa & phòng thủ
[ ] 🏗️ Xây dựng công trình
[ ] 🌦️ Thời tiết & mùa vụ
[ ] 🧩 Hỗ trợ mod (nhân vật, vật phẩm, sự kiện)
👾 Làm bằng tình yêu (và quá nhiều giờ trong terminal)
CLI 1.3 — Phiên bản đầu tiên. Hy vọng các bạn thích! =))
---
