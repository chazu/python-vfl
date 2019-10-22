from vfl.connection import Connection
from vfl.program import Program
from vfl.view import View
from parsimonious.nodes import NodeVisitor

def is_anonymous_node(node):
    return node.expr_name == ''

def value_for_view_name(view_name_node, visited_children):
    return {"type": "view_name",
            "value": view_name_node.text
    }

def value_for_predicate_list_with_parens(node, visited_children):
    import pdb; pdb.set_trace()

node_to_class_map = {
    "program": Program,
    "view": View,
    "connection": Connection
}

node_to_value_map = {
    "viewName": value_for_view_name,
    "predicateListWithParens": value_for_predicate_list_with_parens
}

class VFLVisitor(NodeVisitor):
    def generic_visit(self, node, visited_children):
        if is_anonymous_node(node):
            return visited_children
        if node.expr_name in node_to_class_map.keys():
            return node_to_class_map[node.expr_name](node, visited_children)
        elif node.expr_name in node_to_value_map.keys():
            return node_to_value_map[node.expr_name](node, visited_children)
        else:
            return {'type': node.expr_name,
                    'value': node,
                    'children': visited_children
            }
