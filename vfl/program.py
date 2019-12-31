from util import flatten

from vfl.view import View
from vfl.connection import Connection

class Program:

    def __init__(self, children):
        self.children = children
        self.views = [c for c in self.children if type(c) == View]

        self.name = self._get_name()
        self.preceding_connection = None
        self.following_connection = None
        self.constraints = self._get_constraints()

        # Wire up connections and views
        self.initialize_connections()

    def get_view(self, view_name):
        """Return a child view matching the name passed in."""

        view_names = [view.name for view in self.views]
        index_of_target_view = view_names.index(view_name)

        return self.views[index_of_target_view]

    def initialize_connections(self):
        """ This method is responsible for populating relationships between
        views contained within this program and connections contained within
        this program.

        [view]-[anotherView]
        |-[view]-[anotherView]-[yetAnotherView]-|
        """
        for view in self.views:

            if self._view_is_followed_by_connection(view):
                view.following_connection = self._following_child_for_element(view)
                view.following_connection.preceding_view = view
                view.following_connection.following_view = self._following_child_for_element(view.following_connection)

            if self._view_is_preceded_by_connection(view):
                view.preceding_connection = self._preceding_child_for_element(view)
                view.preceding_connection.following_view = view
                view.preceding_connection.preceding_view = self._preceding_child_for_element(view.preceding_connection)

    def _get_constraints(self):
        return (self.children.get("predicate", None) or
                self.children.get("predicateList", None))

    def _get_name(self):
        try:
            return self.children["name"]
        except StopIteration as e:
            print("ERR: View name not found, this should not be possibble")
            return "anonymousView"

    def _index_of_view(self, view):
        """Return the index of the view in the children of the program."""
        return self.children.index(view)

    def _view_is_followed_by_connection(self, view):
        index_of_view = self._index_of_view(view)
        index_of_following_view = index_of_view + 1

        return (index_of_view + 1 < len(self.children) and
                type(self.children[index_of_following_view]) == Connection)

    def _view_is_preceded_by_connection(self, view):
        index_of_view = self._index_of_view(view)
        index_of_preceding_view = index_of_view - 1

        return (index_of_view - 1 > 0 and
                type(self.children[index_of_preceding_view]) == Connection)

    def _following_child_for_element(self, view):
        index_of_view = self._index_of_view(view)
        return self.children[index_of_view + 1]

    def _preceding_child_for_element(self, view):
        index_of_view = self._index_of_view(view)
        return self.children[index_of_view - 1]
