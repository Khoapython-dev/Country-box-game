#!/usr/bin/env python3
"""
Entry point cho Textual UI
Với error handling và fallback
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Main entry point với error handling"""
    try:
        # Import và chạy Textual UI
        from ui.main_new import main as textual_main
        textual_main()

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("📝 Falling back to CLI version...")
        print()

        # Fallback to CLI
        try:
            from run_cli import main as cli_main
            cli_main()
        except Exception as e2:
            print(f"❌ CLI fallback also failed: {e2}")
            print("🔧 Please check your Python environment and dependencies")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("🔧 Please report this issue")

if __name__ == "__main__":
    main()