from util import flatten
from vfl.predicate import Predicate
from vfl.util import value_of_child_with_type

class Connection:

    __slots__ = ('_node',
                 'children',
                 'following_view',
                 'implicit',
                 'preceding_view',
                 'predicates'
    )

    def __init__(self, children=None):
        if children:
            self.children = list(flatten(children))
            self.predicates = self._init_predicates()
        else:
            self.implicit = True


    def _init_predicates(self):
        p_list = value_of_child_with_type(self.children, 'predicateList')
        return ([Predicate(p) for p in p_list] if p_list
                else [])
