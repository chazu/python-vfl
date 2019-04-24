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

drawing = False
global_points = []
current_mouse_point = None

# Initialize the root console in a context.
app = App()

while True:
    tcod.console_flush()  # Show the console.
    tcod.console_clear(app.root)  # Show the console.    
    for event in tcod.event.wait():
        if event.type == "QUIT":
            raise SystemExit()
        if event.type == "MOUSEBUTTONDOWN":
            global_points.append(event.tile)
            drawing = True
        if event.type == "MOUSEBUTTONUP":
            # Create a proper window and persist it to app's children
            global_points.append(event.tile)
            new_window_points = normalize_points(global_points[0], current_mouse_point)
            new_window = app.make_window(new_window_points[0][0],
                                         new_window_points[0][1],
                                         new_window_points[1][0] - new_window_points[0][0],
                                         new_window_points[1][1] - new_window_points[0][1])
            new_window.persist()

            # Reset relevant state
            global_points = []
            current_mouse_point = None
            drawing = False
        if event.type == "MOUSEMOTION" and drawing:
            current_mouse_point = event.tile
    for item in app.children:
        item.draw()

    # draw the current tile if we're drawing
    if drawing and current_mouse_point:
        window_points  = normalize_points(global_points[0], current_mouse_point)
        current_window = app.make_window(window_points[0][0], window_points[0][1],
                                        window_points[1][0] - window_points[0][0], window_points[1][1] - window_points[0][1])
        current_window.draw()
    
    # print the total number of widgets/rects/windows
    print(app.children)
