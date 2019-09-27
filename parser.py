from parsimonious.grammar import Grammar
from parsimonious.nodes   import NodeVisitor

import pydash as py_
from pydash import flatten
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

def predicate_for_node_type(node_type):
    return lambda x: type(x) == dict and x['type'] == node_type



class VFLVisitor(NodeVisitor):
    def visit_program(self, node, visited_children):
        orientation = py_.find(flatten(visited_children), predicate_for_node_type('orientation'))
        import pdb; pdb.set_trace()
        return {
            "views": py_.filter_(visited_children, predicate_for_node_type('view'))
        }

    def visit_view(self, node, visited_children):
        viewName = py_.find(visited_children, predicate_for_node_type('viewName'))
        result = {
            'type': 'view',
            'name': viewName['value']
        }
        return result

    def visit_viewName(self, node, visited_children):
        return { 'type': 'viewName', 'value': node.text }

    def generic_visit(self, node, visited_children):
        return { 'type': node.expr_name, 'value': node.text, 'children': visited_children }


    # print(GRAMMAR.parse("|-[someview]-|"))
# print(GRAMMAR.parse("[someView]"))
parsed = GRAMMAR.parse("H:[foobar]")

visitor = VFLVisitor()
output = visitor.visit(parsed)
print("Final Output from parsing")
print(output)
