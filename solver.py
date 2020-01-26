from kiwisolver import (Variable as Var,
                        Solver)
VARIABLES = {}

def var_name_for_view_var(view, var_name):
    """Return the string which would be used for the view-specific var.

    For example for the left side of view "quux":

    >>> variable_for_view(v, "left_side")
    >>> "quux_left_side"
    """

    return f"{view.name}_{var_name}"


def get_var(view, var_name):
    """Given a var name, get it from the collection of vars or create it and
    add it to the dict.
    """
    full_var_name = var_name_for_view_var(view, var_name)

    if full_var_name not in VARIABLES:
        VARIABLES[full_var_name] = Var(full_var_name)

    return VARIABLES[full_var_name]


def constraints_for_connection(connection):
    # For a connection between two things in a horizontal layout
    # the right side of the preceding view plus the predicate value
    # equals the left side of the following view. also the left side of the following
    # view minus the predicate value equals the right side of the preceding view
    #
    # For a vertical layout, similar but following is below the preceding.

    # If view is horizontal
    ##
    result = []
    first_view = connection.preceding_view
    first_view.left_side = get_var(first_view, "left_side")
    first_view.right_side = get_var(first_view, "right_side")

    second_view = connection.following_view
    second_view.left_side = get_var(second_view, "left_side")
    second_view.right_side = get_var(second_view, "right_side")


    # Implicit connections have no pedicates
    if connection.implicit:
        print("TOOOOO DOOOOO")
    else:
        raise "REE We're not handling explicit connections yet"


class App:

    def __init__(self):
        self.columns = 50
        self.rows = 50


class ViewSolver:

    def __init__(self, view, app):
        self.app = app
        self.view = view

        self.left_side = Var("left_side")
        self.right_side = Var("right_side")
        self.top = Var("top")
        self.bottom = Var("bottom")
        self._solver = Solver()

        self.constraints = [
            self.left_side == 0,
            self.top == 0,
            self.right_side == self.app.columns,
            self.bottom == self.app.rows,
        ]

        for view in self.view.views:
            view_constraints = [constraints_for_connection(x)
                            for x in view.connections]
            import pdb; pdb.set_trace()

        for c in self.constraints:
            self._solver.addConstraint(c)

        self._solver.updateVariables()

    def repr(self):
        return (f"[[{self.left_side.value()},{self.top.value()}],"
                f"[{self.right_side.value()},{self.bottom.value()}]]")
