class View:

    def __init__(self, children):
        self.children = children
        self.name = self._get_name()
        self.preceding_connection = None
        self.following_connection = None


    def _get_name(self):
        try:
            return self.children["name"]
        except StopIteration as e:
            print("ERR: View name not found, this should not be possibble")
            return "anonymousView"
