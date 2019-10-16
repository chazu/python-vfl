from util import flatten

from vfl.view import View


class Connection:

    def __init__(self, parse_node, children):
        self._node = parse_node
        self.children = children
