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
    print(points)
    if points[1] < points[0]:
        return app.make_window(points[1][0], points[1][1],
                    points[0][0] - points[1][0], points[0][1] - points[1][1])
    else:
        return app.make_window(points[0][0], points[0][1],
                    points[1][0] - points[0][0], points[1][1] - points[0][1])

drawing = False
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
            drawing = True
        if event.type == "MOUSEBUTTONUP":
            # Create a proper window and persist it to app's children
            global_points.append(event.tile)
            new_window = normalize_window(global_points, app)
            new_window.persist()

            # Reset relevant state
            global_points = []
            currentMousePoint = None
            drawing = False
        if event.type == "MOUSEMOTION" and drawing:
            currentMousePoint = event.tile
    for item in app.children:
        item.draw()

    # draw the current tile if we're drawing
    if drawing and currentMousePoint:
        currentWindow = normalize_window([global_points[0], currentMousePoint], app)
        currentWindow.draw()
    
    # print the total number of widgets/rects/windows
    print(app.children)
