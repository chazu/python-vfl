from vfl.connection import Connection
from vfl.view import View

from parsimonious.nodes import NodeVisitor

from util import flatten

relation_map = {
    "==": "equal",
    ">=": "gte",
    "<=": "lte"
}

def roll_up_nested_types(children):
    res = {}
    for child in children:
        res[child["type"]] = child["value"]

    return res


class VFLVisitor(NodeVisitor):

    def visit_program(self, node, visited_children):
        """Returns the overall output."""
        return View(list(flatten(visited_children)))

    def visit_orientation(self, node, visited_children):
        return node.text

    def visit_connection(self, node, visited_children):
        flattened = list(flatten(visited_children))
        return Connection(visited_children)

    def visit_view(self, node, visited_children):
        flattened = list(flatten(visited_children))
        rolled_up = roll_up_nested_types(flattened)
        return View(rolled_up)

    def visit_predicateListWithParens(self, node, visited_children):
        return {
            "type": "predicateList",
            "value": list(flatten(visited_children))
        }

    def visit_predicateList(self, node, visited_children):
        return {
            "type": "predicateList",
            "value": visited_children
        }

    def visit_predicate(self, node, visited_children):
        flattened = list(flatten(visited_children))
        rolled_up = roll_up_nested_types(flattened)

        return {
            "type": "predicate",
            "value": rolled_up
        }

    def visit_objectOfPredicate(self, node, visited_children):
        return {
            "type": "object",
            "value": visited_children[0]
        }

    def visit_simplePredicate(self, node, visited_children):
        return {
            "type": "simplePredicate",
            "value": visited_children[0]
        }

    def visit_priority(self, node, visited_children):
        return {
            "type": "priority",
            "value": int(node.text)
        }

    def visit_number(self, node, visited_children):
        return int(node.text)

    def visit_viewName(self, node, visited_children):
        return {
            "type": "name",
            "value": node.text
        }

    def visit_relation(self, node, visited_children):
        return {
            "type": "relation",
            "value": relation_map[node.text]
        }

    def visit_superview(self, node, visited_children):
        return {
            "type": "superview"
        }

    def visit_(self, node, visited_children):
        return visited_children
