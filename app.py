import tcod
import tcod.event
from window import Window

tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)

class App:
    def __init__(self):
        self.root = tcod.console_init_root(80, 60, order="F")
        self.children = []

    def make_window(self, x0, y0, width, height):
        result = Window(x0, y0, width, height)
        result.app = self
        self.children.append(result)
        return result
