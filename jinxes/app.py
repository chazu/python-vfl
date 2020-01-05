import tcod
import tcod.event

from jinxes.quadtree import Quadtree
from jinxes.window import Window

tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)


class App:
    def __init__(self, columns=80, rows=60):
        self.columns = columns
        self.rows = rows
        self.root = tcod.console_init_root(80, 60, order="F")
        # 0 index in self.children is top window
        self.children = []
        self.quadtree = Quadtree(rows, columns)


    def register_window(self, window):
        self.quadtree.insert(window, window.bbox())
        self.children = [window] + self.children


    def deregister_window(self, window):
        self.children.remove(window)
        self.quadtree.remove(window, window.bbox())


    def move_window_to_top(self, window):
        self.children.remove(window)
        self.children = [window] + self.children


    def move_window(self, window, delta):
        self.deregister_window(window)
        window.origin[0] += delta[0]
        window.origin[1] += delta[1]
        self.register_window(window)


    def make_window(self, x0, y0, width, height):
        result = Window(x0, y0, width, height)
        result.app = self
        return result


    def bbox(self):
        return (0, 0, self.columns, self.rows)


    def windows_at_point(self, point):
        return self.quadtree.query_point(point)


    def top_window_at_point(self, point):
        windows = self.windows_at_point(point)
        with_index = [(self.children.index(x), x) for x in windows]
        sorted_by_index = sorted(with_index)
        return sorted_by_index[0][1]

    def run(self, context):
        while True:
	    tcod.console_flush()  # Show the console.
	    tcod.console_clear(self.root)  # Show the console.

	    for event in tcod.event.wait():
	        try:
	            handler = handler_map[event.type]
	            handler(context, event)
	        except KeyError as e:
	            print(f"unhandled event {e}")

	    for item in reversed(app.children):
	        item.draw()

	    # draw the current tile if we're drawing
	    if (context["mouse_function"] == "DRAW" and
	        context["mousedown_point"] and
	        context["current_mouse_point"]):

	        win_points  = normalize_points(context["mousedown_point"],
	                                       context["current_mouse_point"])
	        cur_window = app.make_window(win_points[0][0],
	                                     win_points[0][1],
	                                     win_points[1][0] - win_points[0][0],
	                                     win_points[1][1] - win_points[0][1])
	        cur_window.draw()
