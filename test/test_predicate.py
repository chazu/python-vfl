import unittest

from vfl.parser import Parser
from vfl.program import Program
from vfl.view import View
from vfl.connection import Connection
from vfl.predicate import Predicate

class TestPredicate(unittest.TestCase):

    def test_simple_predicate(self):
        program = "[testView]-50-[anotherView]"
        result = Parser.parse(program)
        view = result.get_view("testView")
        connection = view.following_connection

        predicate = connection.predicates[0]

        self.assertIsInstance(predicate, Predicate)
