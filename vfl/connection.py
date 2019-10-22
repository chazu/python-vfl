from util import flatten

from vfl.view import View


class Connection:

    __slots__ = ('_node', 'children', 'following_view', 'preceding_view')

    def __init__(self, parse_node, children):
        self._node = parse_node
        self.children = children
