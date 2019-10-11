import unittest

from vfl.parser import Parser
from vfl.program import Program


class TestParser(unittest.TestCase):

    def test_parse_returns_program(self):
        program = "[testView]"
        result = Parser.parse(program)

        self.assertIsInstance(result, Program)

    def test_program_collects_child_views(self):
        program = "[testView]"
        result = Parser.parse(program)
        self.assertEqual(len(result.views), 1)

    def test_view_has_view_name(self):
        program = "[testView]"
        result = Parser.parse(program)
        self.assertEqual(len(result.views), 1)
        self.assertEqual(result.views[0].name, "testView")
