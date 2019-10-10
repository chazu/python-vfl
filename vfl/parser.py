from program import Program
from vfl_visitor import VFLVisitor
from grammar import VFL_GRAMMAR

from pydash import flatten


node_to_class_map = {
    "program": Program
}

# print(GRAMMAR.parse("|-[someview]-|"))
# print(GRAMMAR.parse("[someView]"))

class Parser:

    def __init__(self):
        pass

    @classmethod
    def parse(cls, program):
        parsed = VFL_GRAMMAR.parse(program)

        visitor = VFLVisitor()
        output = visitor.visit(parsed)

        import pdb; pdb.parse()
