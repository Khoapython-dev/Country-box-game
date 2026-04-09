#!/usr/bin/env python3
"""
Test script cho Textual UI
Chạy các test không tương tác trước khi launch TUI
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_textual_components():
    """Test các thành phần Textual UI"""
    print("🧪 Testing Textual UI Components...")

    try:
        from ui.main import TEXTUAL_AVAILABLE, CountryBoxApp, MapView, StatusPanel, MessageLog, CommandInput
        print(f"✅ TEXTUAL_AVAILABLE: {TEXTUAL_AVAILABLE}")

        if not TEXTUAL_AVAILABLE:
            print("⚠️  Textual not available - skipping component tests")
            return False

        # Test app creation
        print("🔧 Testing CountryBoxApp...")
        app = CountryBoxApp()
        print("✅ CountryBoxApp created")

        # Test game state initialization
        print("🔧 Testing game state...")
        from core import game as game_engine
        game_state = game_engine.new_game()
        print("✅ Game state created")

        # Test UI components
        print("🔧 Testing UI components...")
        map_view = MapView(game_state)
        status_panel = StatusPanel(game_state)
        message_log = MessageLog(game_state)
        command_input = CommandInput()
        print("✅ All UI components created")

        # Test rendering (static)
        print("🔧 Testing static rendering...")
        map_render = map_view.render()
        status_render = status_panel.render()
        message_render = message_log.render()
        print("✅ Static rendering successful")

        # Test map viewport
        print("🔧 Testing map viewport...")
        from core import map_render as map_module
        viewport = map_module.render_viewport(45, 37, 20, 10)
        print("✅ Viewport rendering successful")
        print(f"   Sample: {viewport[:50]}...")

        print("\n🎉 All Textual UI components working!")
        return True

    except Exception as e:
        print(f"❌ Component test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_game_integration():
    """Test tích hợp với game engine"""
    print("\n🎮 Testing Game Integration...")

    try:
        from core import game as game_engine
        from ui.main import TEXTUAL_AVAILABLE

        # Create game state
        game_state = game_engine.new_game()
        print("✅ Game state created")

        # Test some commands
        commands_to_test = ["status", "help", "map"]
        for cmd in commands_to_test:
            try:
                game_engine.process_command(game_state, cmd)
                print(f"✅ Command '{cmd}' processed")
            except Exception as e:
                print(f"⚠️  Command '{cmd}' failed: {e}")

        # Test UI integration if Textual available
        if TEXTUAL_AVAILABLE:
            from ui.main import MapView, StatusPanel, MessageLog
            map_view = MapView(game_state)
            status_panel = StatusPanel(game_state)
            message_log = MessageLog(game_state)

            # Test rendering with game state
            map_render = map_view.render()
            status_render = status_panel.render()
            message_render = message_log.render()
            print("✅ UI rendering with game state successful")

        print("🎉 Game integration test passed!")
        return True

    except Exception as e:
        print(f"❌ Game integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("🚀 Country Box - Textual UI Test Suite")
    print("=" * 50)

    # Test components
    component_ok = test_textual_components()

    # Test game integration
    game_ok = test_game_integration()

    print("\n" + "=" * 50)
    if component_ok and game_ok:
        print("🎯 ALL TESTS PASSED!")
        print("💡 Ready to run Textual UI: python run_textual_new.py")
        print("   (This will launch the interactive TUI)")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        print("🔧 Check errors above and fix before running TUI")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)