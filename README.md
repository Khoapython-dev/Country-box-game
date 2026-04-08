# 📦 COUNTRY BOX

> *Xây làng. Nuôi dân. Sinh tồn.*

Một tựa game mô phỏng làng xã chạy trên terminal — bạn ra lệnh cho 10 dân làng
thu thập tài nguyên, chế tạo đồ, và phát triển khu định cư của mình.

---

## 🎮 Cách chơi

Bạn bắt đầu với:
- 👥 **10 dân làng** sẵn sàng làm việc
- 🍖 **10 thức ăn** | 💧 **10 nước uống** | 🪵 Gỗ | 🪨 Đá
- 🗺️ Bản đồ **5x5** để khám phá và xây dựng

Dân làng có thể tự suy nghĩ — nếu đói mà bạn không để ý,
chúng sẽ tự đi săn. Hãy giữ cho chúng no và còn sống!

---

## 💻 Lệnh điều khiển

``` bash 
# Yêu cầu dân làng đi thu thập
hey_village find * [vật phẩm, đồ ăn, thức uống]

# Yêu cầu dân làng chế tạo
hey_village make * [dụng cụ, chế biến đồ ăn]

# Kiểm tra tình trạng dân làng
hey_village are_you_hungry?
# → Tất cả nói "yes"? Nguy rồi. Chúng sắp tự bỏ đi săn.
# → Tất cả nói "no"?  Làng đang ổn định.
🔄 Hệ thống lượt
Mỗi lệnh = 1 lượt. Mỗi lượt:
🍖 Độ đói & 💧 độ khát từ từ giảm
Dân làng rảnh có thể tự hành động
Tài nguyên trên bản đồ hồi phục theo thời gian (dự kiến)
🗺️ Bản đồ
[ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ]
[ ][ ][🏠][ ][ ]
[ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ]
Làng của bạn bắt đầu ở trung tâm. Khám phá ra ngoài để tìm tài nguyên.
📋 Lịch sử cập nhật
Phiên bản
Ghi chú
v1.4 (1.3.6 Beta) by Khoapython-dev:
- Nâng cấp bản đồ lên 20x18
- các thiết yếu ban đầu như: 
+ nước: 15, thức ăn: 15
+ gỗ: 30
+ đá: 30

- các trang bị sẽ được thêm vào:
+ cúp đá (độ bền) 100
+ cúp gỗ: 75
+ rìu đá:100
+ rìu gỗ: 75

- công thức mới:
- 2 đá + 1 gỗ -> cúp/rìu đá (độ bền) +25
- 3 gỗ -> cúp/rìu gỗ (độ bền) +15

- dân làng có thể tự khai thác các tài nguyên này bằng cách di chuyển đến mục tiêu và khai thác 
- dân làng sẽ tự động lấy thức ăn để ăn hồi thanh đói và uống nước 
- sử dụng emoji thay vì ASCII:
- "🏰" toà thị chính (nhà chính cho toàn bộ dân làng)
- "🌲" cây
- "🪨" đá
- "⛰️" núi đá (k thể leo lên hoặc đi qua)
- "🏞️" sông (lấy nước để uống)
nhưng"#" là dân làng k thể đi qua

- khắc phục đồ họa bằng cách sử dụng "clear" để làm mới 
- logic dân làng sẽ được thêm vào sửa chữa riêng ở villager.lua
END

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
