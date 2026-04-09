"""
Textual UI cho Country Box Game
Chuyển từ CLI thuần sang TUI hiện đại với Textual framework
"""

try:
    from textual.app import App, ComposeResult
    from textual.containers import Container, Horizontal, Vertical
    from textual.widgets import Header, Footer, Static, Button, Input, Label
    from textual import events
    TEXTUAL_AVAILABLE = True
except ImportError:
    TEXTUAL_AVAILABLE = False

import asyncio
from core import game as game_engine


if TEXTUAL_AVAILABLE:

    class MapView(Static):
        """Hiển thị map game với viewport"""

        def __init__(self, game_state):
            super().__init__()
            self.game_state = game_state
            self.viewport_width = 80
            self.viewport_height = 20

        def render(self):
            """Render map với viewport"""
            if not self.game_state:
                return "Loading map..."

            player_x = self.game_state["player"]["x"]
            player_y = self.game_state["player"]["y"]

            # Sử dụng viewport rendering từ map_render
            from core import map_render
            map_display = map_render.render_viewport(
                player_x, player_y,
                self.viewport_width, self.viewport_height
            )

            # Thêm thông tin vị trí
            map_info = map_render.get_map_info()
            header = f"Map: {map_info['dimensions']} | Pos: ({player_x}, {player_y}) | Town Hall: {map_info['town_hall']}\n"

            return header + map_display

    class StatusPanel(Static):
        """Panel hiển thị status game"""

        def __init__(self, game_state):
            super().__init__()
            self.game_state = game_state

        def render(self):
            """Render status panel"""
            if not self.game_state:
                return "Loading status..."

            return game_engine.status_report(self.game_state)

    class MessageLog(Static):
        """Log hiển thị messages và events"""

        def __init__(self, game_state):
            super().__init__()
            self.game_state = game_state

        def render(self):
            """Render message log"""
            if not self.game_state or not self.game_state.get("messages"):
                return "No messages yet..."

            # Hiển thị 10 message gần nhất
            messages = self.game_state["messages"][-10:]
            return "\n".join(messages)

    class CommandInput(Input):
        """Input cho commands"""

        def __init__(self):
            super().__init__(placeholder="Enter command (type 'help' for commands)...")

        def on_mount(self):
            """Khi widget được mounted"""
            pass

        async def action_submit(self) -> None:
            """Gọi khi user press Enter"""
            command = self.value.strip()
            if command:
                self.app.process_command(command)
                self.value = ""  # Clear input

    class CountryBoxApp(App):
        """Main Textual App cho Country Box"""

        CSS = """
        Screen {
            background: #1a1a1a;
        }

        Header {
            background: #2d2d2d;
            color: #00ff00;
        }

        Footer {
            background: #2d2d2d;
            color: #ffffff;
        }

        #main-container {
            height: 100%;
        }

        #left-panel {
            width: 25%;
            border-right: solid #444444;
        }

        #right-panel {
            width: 25%;
            border-left: solid #444444;
        }

        #center-panel {
            width: 50%;
        }

        #map-view {
            height: 70%;
            border: solid #444444;
            background: #000000;
            color: #00ff00;
        }

        #command-input {
            height: 1;
            border: solid #444444;
            background: #1a1a1a;
            color: #00ff00;
        }

        #status-panel {
            height: 50%;
            border: solid #444444;
            background: #1a1a1a;
            color: #ffffff;
        }

        #message-log {
            height: 50%;
            border: solid #444444;
            background: #1a1a1a;
            color: #ffff00;
        }

        Button {
            background: #444444;
            color: #ffffff;
        }

        Button:hover {
            background: #666666;
        }
        """

        def __init__(self):
            super().__init__()
            self.game_state = None

        def compose(self) -> ComposeResult:
            """Tạo layout UI"""
            yield Header()
            with Container(id="main-container"):
                with Horizontal():
                    # Left panel - Status
                    with Vertical(id="left-panel"):
                        yield Static("📊 Game Status", id="status-title")
                        status_panel = StatusPanel(self.game_state)
                        status_panel.id = "status-panel"
                        yield status_panel

                    # Center panel - Map & Commands
                    with Vertical(id="center-panel"):
                        yield Static("🗺️ World Map", id="map-title")
                        map_view = MapView(self.game_state)
                        map_view.id = "map-view"
                        yield map_view
                        yield Static("💬 Commands", id="command-title")
                        cmd_input = CommandInput()
                        cmd_input.id = "command-input"
                        yield cmd_input

                    # Right panel - Messages
                    with Vertical(id="right-panel"):
                        yield Static("📝 Messages", id="message-title")
                        msg_log = MessageLog(self.game_state)
                        msg_log.id = "message-log"
                        yield msg_log

            yield Footer()

        async def on_mount(self) -> None:
            """Khởi tạo khi app start"""
            # Khởi tạo game
            self.game_state = game_engine.new_game()
            game_engine.add_message(self.game_state, "🎮 Welcome to Country Box v2.0 - Textual UI!")

            # Update UI
            self.update_ui()

        def update_ui(self):
            """Update tất cả UI components"""
            # Refresh all components that depend on game_state
            self.refresh()

        def process_command(self, command: str):
            """Xử lý command từ user"""
            if not self.game_state:
                return

            # Xử lý command qua game engine
            game_engine.process_command(self.game_state, command)

            # Update UI sau command
            self.update_ui()

        async def on_key(self, event: events.Key) -> None:
            """Handle keyboard shortcuts"""
            if event.key == "ctrl+c":
                self.exit()
            elif event.key == "f1":
                self.process_command("help")


def main():
    """Main entry point"""
    if not TEXTUAL_AVAILABLE:
        print("❌ Textual not installed. Use run_cli.py instead.")
        print("Install with: pip install textual")
        return

    app = CountryBoxApp()
    app.run()


if __name__ == "__main__":
    main()