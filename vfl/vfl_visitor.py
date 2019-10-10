from parsimonious.nodes import NodeVisitor

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
        return node_to_class_map[node.expr_name](node)
        #return { 'type': node.expr_name, 'value': node.text, 'children': visited_children }
