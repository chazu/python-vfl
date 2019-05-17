import pudb
from parsimonious.grammar import Grammar
from parsimonious.nodes   import NodeVisitor

GRAMMAR = Grammar(
    """
    program = (orientation ":")? (superview connection)? view (connection view)* (connection superview)?
    orientation = "H" / "V"
    connection = ("-" predicateList "-") / "-"
    superview = "|"
    view = "[" viewName (predicateListWithParens)? "]"
    predicateListWithParens = "(" predicate ("," predicate)* ")"
    predicateList = simplePredicate / predicateListWithParens
    predicate = relation? objectOfPredicate ("@" priority)?
    objectOfPredicate = constant / viewName
    simplePredicate = number
    priority = ~"[0-9]+"
    constant = number
    number = ~"[\d]+\.[\d]+" / ~"[\d]+"
    viewName = ~"[a-zA-Z]+[a-zA-Z0-9_]*"
    relation = ~"==|>=|<="

    """)

class VFLVisitor(NodeVisitor):
    def visit_program(self, node, visited_children):
        return {
            "views": []
        }
    def visit_view(self, node, visited_children):
        print(node)

    def visit_viewName(self, node, visited_children):
        import pudb; pu.db
        return 

    def visit_orientation(self, node, visited_children):
        print(node)
        
    def generic_visit(self, node, visited_children):
        return node
    
# print(GRAMMAR.parse("|-[someview]-|"))
# print(GRAMMAR.parse("[someView]"))
parsed = GRAMMAR.parse("[foobar]")

visitor = VFLVisitor()
output = visitor.visit(parsed)
