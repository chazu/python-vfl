from vfl.program import Program
from vfl.vfl_visitor import VFLVisitor
from vfl.grammar import VFL_GRAMMAR

from pydash import flatten



class Parser:

    def __init__(self):
        pass

    @classmethod
    def parse(cls, program):
        parsed = VFL_GRAMMAR.parse(program)
        visitor = VFLVisitor()
        output = visitor.visit(parsed)
        return output
