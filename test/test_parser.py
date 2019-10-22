import unittest

from vfl.parser import Parser
from vfl.program import Program
from vfl.view import View
from vfl.connection import Connection

class TestParser(unittest.TestCase):

    def test_parse_returns_program(self):
        program = "[testView]"
        result = Parser.parse(program)

        self.assertIsInstance(result, Program)

    def test_program_collects_child_views(self):
        program = "[testView]"
        result = Parser.parse(program)
        self.assertEqual(len(result.views), 1)
        self.assertEqual(len(result.children), 1)
        self.assertEqual(result.views[0].name, "testView")

    def test_flush_views(self):
        program = "[viewOne][viewTwo]"
        result = Parser.parse(program)
        self.assertEqual(len(result.views), 2)
        self.assertEqual(len(result.children), 2)

    def test_standard_space(self):
        program = "[viewOne]-[viewTwo]"
        result = Parser.parse(program)

        self.assertEqual(len(result.views), 2)
        self.assertEqual(len(result.children), 3)

        expected = [
            View,
            Connection,
            View
        ]

        # Expect order of children
        for idx, item in enumerate(expected):
            self.assertIsInstance(result.children[idx], expected[idx])
