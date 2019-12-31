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

        self.assertIsInstance(test_view.constraints, list)

    def test_connection_to_superview(self):
        program = "|-50-[purpleBox]-50-|"


    def test_get_view(self):
        program = "[testView][anotherView][yetAnotherView]"

        result = Parser.parse(program)

        expected_view_names = [
            "testView",
            "anotherView",
            "yetAnotherView"
        ]

        for view_name in expected_view_names:
            self.assertIsInstance(result.get_view(view_name), View)
            self.assertEqual(result.get_view(view_name).name, view_name)
