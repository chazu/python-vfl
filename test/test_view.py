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

    def test_implicit_connection(self):
        program = "[view1][view2]"
        result = Parser.parse(program)

        view_one = result.get_view("view1")

        self.assertIsInstance(view_one.following_connection, Connection)

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

    # TODO assert that the connection between testView and superview is
    # implicit - no hyphen needed
    def test_view_implicit_connection_to_superview(self):
        program = "|-10-[testView]|"


    # def test_view_left_margin_zero(self):
    #     program = "[testView]"
    #     result = Parser.parse(program)

    #     test_view = result.get_view("testView")
    #     self.assertEqual(test_view.left_margin, 0)

    # def test_view_left_margin_ten(self):
    #     program = "|-10-[testView]-|"
    #     result = Parser.parse(program)

    #     test_view = result.get_view("testView")
    #     self.assertEqual(test_view.left_margin, 10)
