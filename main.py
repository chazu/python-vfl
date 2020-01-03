"""
Make sure 'arial10x10.png' is in the same directory as this script.
"""

import tcod
import tcod.event

from jinxes.app import App
from util import normalize_points

MOUSE_FUNCTIONS = [
    "DRAW",
    "DRAG"
]
# Setup the font
tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)

interaction_context = {
    "current_mouse_point": None,
    "mouse_function": None,
    "mousedown_point": None
}

# Initialize the root console in a context.
def mouse_function_for_event(app, event):
    return "DRAG" if app.window_at_point(event.tile) else "DRAW"


def handle_quit(context, event):
    raise SystemExit()


def handle_mouse_down(context, event):
    context["mousedown_point"] = event.tile
    context["mouse_function"] = mouse_function_for_event(context["app"], event)
    context["current_mouse_point"] = event.tile

    print(context)

def handle_mouse_move(context, event):
        context["current_mouse_point"] = event.tile


def handle_mouse_up(context, event):

    if context["mouse_function"] == "DRAW":
        # Create a proper window and persist it to app's children
        win_points = normalize_points(context["mousedown_point"],
                                      context["current_mouse_point"])

        new_window = app.make_window(win_points[0][0],
                                     win_points[0][1],
                                     win_points[1][0] - win_points[0][0],
                                     win_points[1][1] - win_points[0][1])
        app.register_window(new_window)

    # Reset relevant state
    context["mousedown_point"] = None
    context["current_mouse_point"] = None
    context["mouse_function"] = None


handler_map = {
    "QUIT": handle_quit,
    "MOUSEBUTTONDOWN": handle_mouse_down,
    "MOUSEBUTTONUP": handle_mouse_up,
    "MOUSEMOTION": handle_mouse_move
}

app = App()
interaction_context["app"] = app

while True:
    tcod.console_flush()  # Show the console.
    tcod.console_clear(app.root)  # Show the console.

    for event in tcod.event.wait():
        print(event.type)
        try:
            handler = handler_map[event.type]
            handler(interaction_context, event)
        except KeyError as e:
            print(f"unhandled event {e}")

    for item in reversed(app.children):
        item.draw()

    # draw the current tile if we're drawing
    if (interaction_context["mouse_function"] == "DRAW" and
        interaction_context["mousedown_point"] and
        interaction_context["current_mouse_point"]):

        win_points  = normalize_points(interaction_context["mousedown_point"],
                                       interaction_context["current_mouse_point"])
        cur_window = app.make_window(win_points[0][0],
                                     win_points[0][1],
                                     win_points[1][0] - win_points[0][0],
                                     win_points[1][1] - win_points[0][1])
        cur_window.draw()
