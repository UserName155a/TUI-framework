# Text based RPG-type app


from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.binding import Binding

class Hello(Widget):
    def render(self) -> RenderResult:
        return "Hello, [b]world[/b]"

class Main(App):

    BINDINGS = [
        ("d","quit","exit app")
        ]

    def compose(self) -> ComposeResult:
        yield Hello()

    def on_mount(self) -> None: #right after launch
        self.screen.styles.background = "black"
        self.grid = []

if __name__ == "__main__":
    app = Main()
    app.run()
