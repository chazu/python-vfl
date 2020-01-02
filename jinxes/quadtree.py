from pyqtree import Index


class Quadtree:

    __slots__ = (
        "rows",
        "columns",
        "_quadtree"
    )

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self._quadtree = Index(bbox=(0, 0, columns, rows))

    def query_point(self, point):
        return self._quadtree.intersect(point + point)

    def query_rect(self,bbox):
        return self._quadtree.intersect(bbox)

    def insert(self, obj, bbox):
        return self._quadtree.insert(obj, bbox)
