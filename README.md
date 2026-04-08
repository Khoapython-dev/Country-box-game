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

# Yêu cầu dân làng chế tạo
hey_village make * [axe|axe_wood|axe_stone|pickaxe|pickaxe_wood|pickaxe_stone|food]

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
