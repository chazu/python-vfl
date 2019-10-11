from util import flatten

from vfl.view import View


class Program:

    def __init__(self, parse_node, children):
        self._node = parse_node
        self._children = children
        self.views = [c for c in flatten(children) if type(c) == View]
