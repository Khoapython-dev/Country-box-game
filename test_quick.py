#!/usr/bin/env python3
"""Quick test để kiểm tra import và render."""

import sys
sys.path.insert(0, '/workspaces/Country-box-game')

try:
    from core import game, map_render, commands
    print("✓ Import OK")
    
    # Test map render
    print("\nTest render map:")
    map_render.render(10, 9)
    
    # Test new_game
    g = game.new_game()
    print(f"\n✓ new_game() OK - Turn: {g['turn']}, Player: {g['player']}")
    print(f"✓ Inventory: Food={g['inventory']['food']}, Wood={g['inventory']['wood']}")
    
    # Test command parse
    ac, ar = commands.parse_command("hey_village find * wood")
    print(f"\n✓ parse_command OK - Action: {ac}, Args: {ar}")
    
    print("\n✓ All tests passed!")
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
