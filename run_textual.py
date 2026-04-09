#!/usr/bin/env python3
"""
Country Box v2.0 - Textual UI Entry Point
Chạy game với giao diện Textual hiện đại
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from ui.main import main
    main()
except ImportError as e:
    print(f"❌ Lỗi import: {e}")
    print("Vui lòng cài đặt Textual: pip install textual")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n👋 Tạm biệt!")
    sys.exit(0)