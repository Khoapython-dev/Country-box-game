#!/usr/bin/env python3
"""
Country Box Game Launcher
Script khởi động game với các tùy chọn
"""

import subprocess
import sys
import os

def print_menu():
    """Hiển thị menu lựa chọn"""
    print("🎮 COUNTRY BOX v2.0 - Game Launcher")
    print("=" * 50)
    print("Chọn chế độ chơi:")
    print("1. 🎭 Textual UI (Khuyến nghị) - TUI hiện đại")
    print("2. 💻 CLI Mode - Dòng lệnh thuần")
    print("3. 🎯 Demo - Xem demo UI")
    print("4. 🧪 Test Suite - Chạy test")
    print("5. 📚 Help - Hướng dẫn chơi")
    print("6. ❌ Exit")
    print("=" * 50)

def run_command(cmd_list):
    """Chạy command và xử lý kết quả"""
    try:
        print(f"🚀 Đang khởi động: {' '.join(cmd_list)}")
        print("-" * 50)
        result = subprocess.run(cmd_list)
        return result.returncode
    except KeyboardInterrupt:
        print("\n👋 Đã dừng game")
        return 0
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return 1

def show_help():
    """Hiển thị hướng dẫn chơi"""
    print("📚 HƯỚNG DẪN CHƠI COUNTRY BOX v2.0")
    print("=" * 50)
    print("🎯 MỤC TIÊU:")
    print("  Xây làng, nuôi dân, sinh tồn qua các lượt")
    print()
    print("🏠 BẮT ĐẦU:")
    print("  - 10 dân làng, 15 thức ăn/nước, 30 gỗ/đá")
    print("  - Town Hall ở trung tâm map 90x75")
    print()
    print("🎛️ LỆNH CƠ BẢN:")
    print("  status          - Xem tình trạng game")
    print("  map             - Xem map xung quanh")
    print("  help            - Xem tất cả lệnh")
    print()
    print("👥 ĐIỀU KHIỂN DÂN LÀNG:")
    print("  hey_village find * [wood|stone|food|water]")
    print("  hey_village make * [axe_wood|axe_stone|food]")
    print("  hey_village trade * item amount")
    print()
    print("💡 MẸO:")
    print("  - Theo dõi độ đói/khát của dân làng")
    print("  - Khai thác tài nguyên để chế tạo công cụ")
    print("  - Xây smelter để luyện sắt/thép")
    print("  - Mua bán với thương nhân khi có")
    print()
    print("🎮 TRONG TEXTUAL UI:")
    print("  - 3 panel: Status | Map+Commands | Messages")
    print("  - Gõ lệnh vào ô command và Enter")
    print("  - Ctrl+C để thoát")
    print("=" * 50)

def main():
    """Main launcher function"""
    while True:
        print_menu()
        try:
            choice = input("Nhập lựa chọn (1-6): ").strip()

            if choice == "1":
                # Textual UI
                cmd = ["/usr/bin/python3", "run_textual_new.py"]
                run_command(cmd)

            elif choice == "2":
                # CLI Mode
                cmd = ["/usr/bin/python3", "run_cli.py"]
                run_command(cmd)

            elif choice == "3":
                # Demo
                cmd = ["/usr/bin/python3", "demo_textual.py"]
                run_command(cmd)

            elif choice == "4":
                # Test Suite
                cmd = ["/usr/bin/python3", "test_textual_ui.py"]
                run_command(cmd)

            elif choice == "5":
                # Help
                show_help()
                input("\nNhấn Enter để tiếp tục...")

            elif choice == "6":
                # Exit
                print("👋 Tạm biệt!")
                break

            else:
                print("❌ Lựa chọn không hợp lệ. Nhập số từ 1-6.")

        except KeyboardInterrupt:
            print("\n👋 Tạm biệt!")
            break
        except Exception as e:
            print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    main()