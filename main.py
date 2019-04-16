# Make sure 'arial10x10.png' is in the same directory as this script.
import tcod
import tcod.event

from window import Window
from app import App

# Setup the font.
tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)

def normalize_window(points, app):
    if points[1] < points[0]:
        return app.make_window(points[1][0], points[1][1],
                    points[0][0] - points[1][0], points[0][1] - points[1][1])
    else:
        return app.make_window(points[0][0], points[0][1],
                    points[1][0] - points[0][1], points[1][1] - points[0][1])

global_points = []
currentMousePoint = None

# Initialize the root console in a context.
app = App()

while True:
    tcod.console_flush()  # Show the console.
    for event in tcod.event.wait():
        if event.type == "QUIT":
            raise SystemExit()
        if event.type == "MOUSEBUTTONDOWN":
            global_points.append(event.tile)
            print("oof")
        if event.type == "MOUSEBUTTONUP":
            print("ouch")
            global_points.append(event.tile)
            normalize_window(global_points, app)
            global_points = []
    for item in app.children:
        item.draw()

