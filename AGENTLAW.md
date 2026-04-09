# Luật:
```
1. Thực hiện đúng quy trình: code -> test -> lỗi thì fix tiếp, k lỗi thì ok
2. cố gắng hình dung và suy nghĩ nhiều hơn 
3. không code dỡ
4. nếu tạo các file k liên quan đến dự án hay test thì test sẽ phải xoá (không được xoá .md, .json, .lua, ... nếu k lq)
5. Hãy sắp xếp lại tổ chức file/dir
- nếu là mod -> thêm vào mods/private/<name>.lua
- nếu là logic/nhân vật viết bằng lua -> vào entities/.lua
- nếu là code engine, hãy tự phân từng dir với chức năng 
- nếu là .json hay file cấu hình, sự kiện, ... thì vào data/.(json/toml/conf,...)
```