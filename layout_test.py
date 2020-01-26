# Python imports


# Third-party imports
import tcod
import tcod.event

# First-Party Imports
from jinxes.app import App
from solver import ViewSolver
from vfl.parser import Parser


# Setup the font
tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)


def handle_quit(context, event):
    """Quit the program."""
    raise SystemExit()

handler_map = {
    "QUIT": handle_quit,
}

app = App()

program = "[view][lol]"
parsed = Parser.parse(program)

viewsolver = ViewSolver(parsed, app)

# while True:
#     tcod.console_flush()  # Show the console.
#     tcod.console_clear(app.root)  # Show the console.

#     for event in tcod.event.wait():
#         try:
#             handler = handler_map[event.type]
#             handler(None, event)
#         except KeyError as e:
#             print(f"unhandled event {e}")

#     for item in reversed(app.children):
#         item.draw()
