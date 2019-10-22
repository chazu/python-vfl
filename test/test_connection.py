import unittest

from vfl.parser import Parser
from vfl.program import Program
from vfl.view import View
from vfl.connection import Connection


class TestConnection(unittest.TestCase):

    def test_basic_connection(self):
        program = "[viewOne]-[viewTwo]"
        result = Parser.parse(program)

        view_one = result.views[0]
        view_two = result.views[1]

        self.assertEquals(view_one.name, "viewOne")
        self.assertEquals(view_two.name, "viewTwo")

        self.assertIsInstance(view_one, View)
        self.assertIsNone(view_one.preceding_connection)
        self.assertIsInstance(view_one.following_connection, Connection)
        self.assertEquals(view_one.following_connection.following_view,
                          view_two)
        self.assertEquals(view_one.following_connection.preceding_view,
                          view_one)


        self.assertIsInstance(view_two, View)
        self.assertIsInstance(view_two.preceding_connection, Connection)
        self.assertIsNone(view_two.following_connection)
        self.assertEquals(view_two.preceding_connection.preceding_view,
                          view_one)
        self.assertEquals(view_two.preceding_connection.following_view,
                          view_two)
