import unittest

from vfl.parser import Parser
from vfl.program import Program
from vfl.view import View
from vfl.connection import Connection


class TestView(unittest.TestCase):

    def test_view_width_constraint(self):
        program = "[testView(>=50)]"
        result = Parser.parse(program)

        test_view = result.get_view("testView")
        self.assertIsInstance(test_view, View)

        self.assertEquals(test_view.width_constraint, 50)
        self.assertEquals(test_view.width_constraint_operator, "=")
