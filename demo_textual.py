#!/usr/bin/env python3
"""
Demo script cho Textual UI
Hiển thị UI components mà không cần tương tác
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def demo_ui():
    """Demo UI components"""
    print("🎭 Country Box - Textual UI Demo")
    print("=" * 50)

    try:
        from ui.main import TEXTUAL_AVAILABLE
        if not TEXTUAL_AVAILABLE:
            print("❌ Textual not available")
            return

        from ui.main import MapView, StatusPanel, MessageLog
        from core import game as game_engine

        # Create game state
        game_state = game_engine.new_game()

        # Add some test messages
        game_engine.add_message(game_state, "🏠 Welcome to your village!")
        game_engine.add_message(game_state, "👥 Population: 5 villagers")
        game_engine.add_message(game_state, "🌾 Resources: Food=50, Water=50")

        # Process some commands to generate activity
        game_engine.process_command(game_state, "turn")  # Advance a turn
        game_engine.process_command(game_state, "status")

        print("📊 Game Status:")
        print("-" * 30)
        status_panel = StatusPanel(game_state)
        status_render = status_panel.render()
        print(status_render)

        print("\n🗺️ Map View (Viewport):")
        print("-" * 30)
        map_view = MapView(game_state)
        map_render = map_view.render()
        print(map_render)

        print("\n📝 Message Log:")
        print("-" * 30)
        message_log = MessageLog(game_state)
        message_render = message_log.render()
        print(message_render)

        print("\n🎉 Demo completed successfully!")
        print("💡 To run interactive TUI: python run_textual_new.py")

    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo_ui()