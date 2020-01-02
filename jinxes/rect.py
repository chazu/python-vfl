class Rect:
    def __init__(self, x0, y0, w, h, app=None):
        self.app = app if app else None

        self.origin = [x0, y0]
        self.w = w
        self.h = h

    def draw(self, x, y):
        pass

