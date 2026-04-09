#!/usr/bin/env python3
"""
Test script để kiểm tra Textual UI components
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    print("Testing imports...")
    from core import game
    print("✅ core.game imported")

    from core import map_render
    print("✅ core.map_render imported")

    from ui.main import CountryBoxApp
    print("✅ ui.main imported")

    # Test game creation
    print("\nTesting game creation...")
    g = game.new_game()
    print(f"✅ Game created with {len(g['villagers'])} villagers")

    # Test map info
    print("\nTesting map...")
    map_info = map_render.get_map_info()
    print(f"✅ Map: {map_info['dimensions']}")
    print(f"✅ Town hall at: {map_info['town_hall']}")

    # Test viewport rendering
    print("\nTesting viewport rendering...")
    viewport = map_render.render_viewport(45, 37, 10, 5)
    print("✅ Viewport rendered:")
    print(viewport[:200] + "...")

    print("\n🎉 All tests passed! Textual UI ready to run.")

except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages:")
    print("pip install textual")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()