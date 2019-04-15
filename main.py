# Make sure 'arial10x10.png' is in the same directory as this script.
import tcod
import tcod.event

# Setup the font.
tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)

class Rect:
    def __init__(self, x0, y0, width, height):
        self.origin = [x0, y0]
        self.width  = width
        self.height = height

    def str(self):
        return "Origin: " + self.origin +  "Width: " + self.width + "Height: " + self.height


def create_rect():
    if points[1] < points[0]:
        rects.append(Rect(points[1][0], points[1][1],
                          points[0][0] - points[1][0], points[0][1] - points[1][1]))
    else:
        rects.append(Rect(points[0][0], points[0][1],
                          points[1][0] - points[0][1], points[1][1] - points[0][1]))

    print(rects[0])

drawing = False
rects = []
points = []
# Initialize the root console in a context.
with tcod.console_init_root(80, 60, order="F") as root_console:
    while True:
        tcod.console_flush()  # Show the console.
        for event in tcod.event.wait():
            if event.type == "QUIT":
                raise SystemExit()
            if event.type == "MOUSEBUTTONDOWN":
                points.append(event.tile)
            if event.type == "MOUSEBUTTONUP":
                points.append(event.tile)
                create_rect()
                points = []
        for rect in rects:
            root_console.print_frame(rect.origin[0], rect.origin[1], rect.width, rect.height)

