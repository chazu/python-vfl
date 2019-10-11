from vfl.program import Program
from vfl.view import View
from parsimonious.nodes import NodeVisitor

def value_for_view_name(view_name_node, visited_children):
    return {"type": "view_name",
            "value": view_name_node.text
    }

node_to_class_map = {
    "program": Program,
    "view": View
}

node_to_value_map = {
    "viewName": value_for_view_name
}

class VFLVisitor(NodeVisitor):
    # def visit_program(self, node, visited_children):
    #     orientation = py_.find(flatten(visited_children), predicate_for_node_type('orientation'))
    #     return {
    #         "views": py_.filter_(visited_children, predicate_for_node_type('view'))
    #     }

    # def visit_view(self, node, visited_children):
    #     viewName = py_.find(visited_children, predicate_for_node_type('viewName'))
    #     result = {
    #         'type': 'view',
    #         'name': viewName['value']
    #     }
    #     return result
    # def visit_viewName(self, node, visited_children):
    #     return { 'type': 'viewName', 'value': node.text }

    def generic_visit(self, node, visited_children):
        if node.expr_name in node_to_class_map.keys():
            return node_to_class_map[node.expr_name](node, visited_children)
        elif node.expr_name in node_to_value_map.keys():
            return node_to_value_map[node.expr_name](node, visited_children)
        else:
            return None
        #return { 'type': node.expr_name, 'value': node.text, 'children': visited_children }
