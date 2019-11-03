# Make sure 'arial10x10.png' is in the same directory as this script.
import tcod
import tcod.event

from app import App
from util import normalize_points
from window import Window

# Setup the font.
tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)

context = {
    "current_mouse_point": None,
    "drawing": False,
    "global_points": []
}

# Initialize the root console in a context.
app = App()
drawing = False

def handle_quit(context, event):
    raise SystemExit()

def handle_mouse_down(context, event):
    context["global_points"].append(event.tile)
    context["drawing"] = True

def handle_mouse_move(context, event):
    if context["drawing"]:
        context["current_mouse_point"] = event.tile

def handle_mouse_up(context, event):
        # Create a proper window and persist it to app's children
        context["global_points"].append(event.tile)
        win_points = normalize_points(context["global_points"][0],
                                      context["current_mouse_point"])

        new_window = app.make_window(win_points[0][0],
                                     win_points[0][1],
                                     win_points[1][0] - win_points[0][0],
                                     win_points[1][1] - win_points[0][1])
        new_window.persist()

        # Reset relevant state
        context["global_points"] = []
        context["current_mouse_point"] = None
        drawing = False

handler_map = {
    "QUIT": handle_quit,
    "MOUSEBUTTONDOWN": handle_mouse_down,
    "MOUSEBUTTONUP": handle_mouse_up,
    "MOUSEMOTION": handle_mouse_move
}

while True:
    tcod.console_flush()  # Show the console.
    tcod.console_clear(app.root)  # Show the console.

    for event in tcod.event.wait():
        print(event.type)
        try:
            handler = handler_map[event.type]
            handler(context, event)
        except KeyError as e:
            print(f"unhandled event {e}")

    for item in app.children:
        item.draw()

    # draw the current tile if we're drawing
    if (context["drawing"] and context["current_mouse_point"]
        and context["global_points"]):

        win_points  = normalize_points(context["global_points"][0],
                                       context["current_mouse_point"])
        cur_window = app.make_window(win_points[0][0],
                                     win_points[0][1],
                                     win_points[1][0] - win_points[0][0],
                                     win_points[1][1] - win_points[0][1])
        cur_window.draw()
