"""
UI package cho Country Box Game
Textual-based terminal UI
"""

try:
    from .main import TEXTUAL_AVAILABLE
    if TEXTUAL_AVAILABLE:
        from .main import CountryBoxApp, main
        __all__ = ["CountryBoxApp", "main", "TEXTUAL_AVAILABLE"]
    else:
        __all__ = ["TEXTUAL_AVAILABLE"]
        # CLI fallback - no Textual classes
        def main():
            print("❌ Textual not available. Use run_cli.py instead.")
except ImportError:
    # Fallback if main.py fails to import
    TEXTUAL_AVAILABLE = False
    __all__ = ["TEXTUAL_AVAILABLE"]
    def main():
        print("❌ UI module failed to load. Check dependencies.")