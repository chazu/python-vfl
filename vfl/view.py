class View:

    def __init__(self, node, children):
        self._node = node
        self._children = children
        self.name = self._get_name()

    def _get_name(self):
        try:
            # TODO This is gross AF
            return [x for x in self._children
                         if x and x['type'] == 'view_name'][0]['value']
        except StopIteration as e:
            print("ERR: View name not found, this should not be possibble")
            return "anonymousView"
