import unittest

from vfl.parser import Parser
from vfl.program import Program
from vfl.view import View
from vfl.connection import Connection

class TestProgram(unittest.TestCase):

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
