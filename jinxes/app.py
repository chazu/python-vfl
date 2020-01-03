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
        self.children = []
        self.quadtree = Quadtree(rows, columns)

    def register_window(self, window):
        self.quadtree.insert(window, window.bbox())
        self.children = [window] + self.children

    def move_window_to_top(self, window):
        self.children.remove(window)
        self.children = [window] + self.children


    def make_window(self, x0, y0, width, height):
        result = Window(x0, y0, width, height)
        result.app = self
        return result

    def bbox(self):
        return (0, 0, self.columns, self.rows)

    def window_at_point(self, point):
        points =  self.quadtree.query_point(point)
        return points[0] if any(points) else None
