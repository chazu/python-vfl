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
    "app": None,
    "current_mouse_point": None,
    "previous_mouse_point": None,
    "mouse_delta": None,
    "mouse_function": None,
    "mousedown_point": None,
    "selected_window": None
}

def mouse_delta(context):
    if not context["previous_mouse_point"]:
        return (0, 0)

    delta_x = context["current_mouse_point"][0] - context["previous_mouse_point"][0]
    delta_y = context["current_mouse_point"][1] - context["previous_mouse_point"][1]

    return (delta_x, delta_y)


def mouse_function_for_event(app, event):
    """Determine what dragging does based on window presence."""
    return "DRAG" if app.windows_at_point(event.tile) else "DRAW"


def handle_quit(context, event):
    raise SystemExit()


def nonzero_mouse_delta(delta):
    try:
        return delta[0] != 0 or delta[1] != 0
    except KeyError:
        return False


def handle_mouse_down(context, event):
    context["mousedown_point"] = event.tile
    context["mouse_function"] = mouse_function_for_event(context["app"], event)
    context["current_mouse_point"] = event.tile

    if context["mouse_function"] == "DRAG":
        context["selected_window"] = context["app"].top_window_at_point(event.tile)

def handle_mouse_move(context, event):

    if context["current_mouse_point"]:
        context["previous_mouse_point"] = (context["current_mouse_point"][0],
                                           context["current_mouse_point"][1])
    context["current_mouse_point"] = event.tile
    context["mouse_delta"] = mouse_delta(context)



    # TODO If mouse_delta is non-zero and we're dragging, move the selected window to front and
    # move its origin
    if context["mouse_function"] == "DRAG" and nonzero_mouse_delta(context["mouse_delta"]):
        context["selected_window"].origin[0] += context["mouse_delta"][0]
        context["selected_window"].origin[1] += context["mouse_delta"][1]


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
    context["mouse_function"] = None
    context["selected_window"] = None
    context["mouse_delta"] = None

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
