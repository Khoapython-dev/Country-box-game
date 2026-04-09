#!/usr/bin/env python3
"""
Debug script để tìm lỗi import
"""

import sys
import os

print("Python version:", sys.version)
print("Current dir:", os.getcwd())
print("Python path:", sys.path)

try:
    print("\nTesting textual import...")
    from textual.app import App
    print("✅ Textual imported successfully")
except ImportError as e:
    print(f"❌ Textual import failed: {e}")
    print("Please install: pip install textual")
    sys.exit(1)

try:
    print("\nTesting core imports...")
    from core import game
    print("✅ core.game imported")
except ImportError as e:
    print(f"❌ core.game import failed: {e}")
    sys.exit(1)

try:
    from core import map_render
    print("✅ core.map_render imported")
except ImportError as e:
    print(f"❌ core.map_render import failed: {e}")
    sys.exit(1)

try:
    print("\nTesting UI imports...")
    from ui.main import CountryBoxApp
    print("✅ ui.main imported")
except ImportError as e:
    print(f"❌ ui.main import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n🎉 All imports successful!")