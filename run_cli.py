#!/usr/bin/env python3
"""
Country Box v2.0 - CLI Fallback
Chạy game với CLI đơn giản trong khi debug Textual UI
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from core import game as game_engine
from core import map_render

def show_game_state(game_state):
    """Hiển thị trạng thái game với map viewport"""
    print("\n" + "="*80)
    print("COUNTRY BOX v2.0 - CLI Mode")
    print("="*80)

    # Map viewport
    player_x = game_state["player"]["x"]
    player_y = game_state["player"]["y"]

    print(f"\n🗺️ MAP VIEWPORT (around player at {player_x},{player_y}):")
    viewport = map_render.render_viewport(player_x, player_y, 40, 15)
    print(viewport)

    # Status
    print(f"\n📊 STATUS:")
    print(game_engine.status_report(game_state))

    # Messages
    print(f"\n📝 RECENT MESSAGES:")
    messages = game_state.get("messages", [])[-5:]
    if messages:
        for msg in messages:
            print(f"  {msg}")
    else:
        print("  No messages yet")

def main():
    """Main CLI game loop"""
    print("🎮 Starting Country Box v2.0 (CLI Mode)...")

    # Initialize game
    game_state = game_engine.new_game()
    game_engine.add_message(game_state, "🎮 Welcome to Country Box v2.0 - CLI Mode!")
    game_engine.add_message(game_state, "💡 Use commands like: hey_village find * wood")
    game_engine.add_message(game_state, "💡 Type 'help' for all commands")

    while True:
        show_game_state(game_state)

        try:
            command = input("\n> ").strip()
            if command.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break

            # Process command
            game_engine.process_command(game_state, command)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            game_engine.add_message(game_state, f"❌ Command error: {e}")

if __name__ == "__main__":
    main()