class View:

    __slots__ = ('children',
                 'name',
                 'preceding_connection',
                 'following_connection',
                 'constraints')
    def __init__(self, children):
        self.children = children
        self.name = self._get_name()
        self.preceding_connection = None
        self.following_connection = None
        self.constraints = self._get_constraints()

    def _get_constraints(self):
        return (self.children.get("predicate", None) or
                self.children.get("predicateList", None))

    def _get_name(self):
        try:
            return self.children["name"]
        except StopIteration as e:
            print("ERR: View name not found, this should not be possibble")
            return "anonymousView"
