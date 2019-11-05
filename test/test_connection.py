import unittest

from vfl.parser import Parser
from vfl.predicate import Predicate
from vfl.program import Program
from vfl.view import View
from vfl.connection import Connection


class TestConnection(unittest.TestCase):

    def test_basic_connection(self):
        program = "[viewOne]-[viewTwo]"
        result = Parser.parse(program)

        view_one = result.views[0]
        view_two = result.views[1]

        connection = result.views[0].following_connection

        # Make sure its the same connection instance attached to both
        # view instances
        self.assertEqual(connection, result.views[1].preceding_connection)

        # Assert that theres no connections where there shouldn't be
        self.assertIsNone(view_one.preceding_connection)
        self.assertIsNone(view_two.following_connection)

        self.assertIsInstance(view_one.following_connection, Connection)
        self.assertIsInstance(view_two.preceding_connection, Connection)

        self.assertEquals(connection.following_view, view_two)
        self.assertEquals(connection.preceding_view, view_one)


    def test_connection_with_predicate(self):
        program = "[viewOne]-50-[viewTwo]"
        result = Parser.parse(program)

        connection = result.views[0].following_connection
        self.assertIsInstance(connection.predicates, list)
        self.assertTrue(len(connection.predicates) == 1)
        self.assertIsInstance(connection.predicates[0], Predicate)
