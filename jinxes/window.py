class Window:
    def __init__(self, x0, y0, w, h, app=None):
        self.app = app if app else None

        self.origin = [x0, y0]
        self.w = w
        self.h = h

    def draw(self):
        self.app.root.print_frame(self.origin[0], self.origin[1], self.w, self.h)

    def persist(self):
        self.app.children.append(self)

    def bbox(self):
        return (self.origin[0], self.origin[1],
                self.origin[0] + self.w, self.origin[1] + self.h)
