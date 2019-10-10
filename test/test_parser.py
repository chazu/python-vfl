import unittest

from vfl.parser import Parser
from vfl.program import Program


class TestParser(unittest.TestCase):

    def test_parse_single_view_program(self):
        program = "[testView]"
        result = Parser.parse(program)
        self.assertIsInstance(result, Program)
