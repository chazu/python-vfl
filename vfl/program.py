from vfl.view import View
class Program:

    def __init__(self, parse_node, children):
        self._node = parse_node
        self._children = children
        self.views = [c for c in children if type(c) == View]
