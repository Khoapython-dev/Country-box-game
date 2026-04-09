#!/usr/bin/env python3
"""
Test script để kiểm tra imports và dependencies
"""

import sys
import os

def test_imports():
    """Test all required imports"""
    print("🔍 Testing imports...")

    # Test core modules
    try:
        import core.game as game_engine
        print("✅ core.game imported successfully")
    except ImportError as e:
        print(f"❌ core.game import failed: {e}")
        return False

    try:
        import core.map_render as map_render
        print("✅ core.map_render imported successfully")
    except ImportError as e:
        print(f"❌ core.map_render import failed: {e}")
        return False

    # Test Textual (optional)
    try:
        from textual.app import App
        from textual.widgets import Static
        print("✅ Textual framework available")
        textual_available = True
    except ImportError:
        print("⚠️  Textual framework not available - will use CLI fallback")
        textual_available = False

    # Test game initialization
    try:
        game_state = game_engine.new_game()
        print("✅ Game initialization successful")
        print(f"   Map size: {len(game_state['map'])}x{len(game_state['map'][0])}")
        print(f"   Player position: ({game_state['player']['x']}, {game_state['player']['y']})")
    except Exception as e:
        print(f"❌ Game initialization failed: {e}")
        return False

    # Test map rendering
    try:
        from core.map_render import render_viewport
        viewport = render_viewport(45, 37, 20, 10)  # Center of 90x75 map
        print("✅ Map viewport rendering successful")
        print("   Sample viewport:")
        print(viewport[:200] + "..." if len(viewport) > 200 else viewport)
    except Exception as e:
        print(f"❌ Map rendering failed: {e}")
        return False

    print("\n🎉 All core functionality working!")
    print(f"   Textual UI: {'Available' if textual_available else 'Not available (CLI fallback)'}")

    return True

def test_ui():
    """Test UI components"""
    print("\n🔍 Testing UI components...")

    try:
        from ui.main_new import TEXTUAL_AVAILABLE
        print(f"✅ UI module loaded, Textual available: {TEXTUAL_AVAILABLE}")

        if TEXTUAL_AVAILABLE:
            print("✅ Textual UI ready to run")
        else:
            print("⚠️  CLI fallback will be used")

    except Exception as e:
        print(f"❌ UI test failed: {e}")
        return False

    return True

if __name__ == "__main__":
    print("🚀 Country Box Game - Dependency Test")
    print("=" * 50)

    success = test_imports()
    if success:
        test_ui()

    print("\n" + "=" * 50)
    if success:
        print("🎯 Ready to run! Use:")
        print("   python run_textual_new.py  # Textual UI (with CLI fallback)")
        print("   python run_cli.py          # CLI only")
    else:
        print("❌ Issues found - please fix before running")