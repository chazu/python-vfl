from kiwisolver import (Variable as Var,
                        Solver)


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

    import pdb; pdb.set_trace()
    if connection.implicit:

    for p in connection.predicates:
        pass


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
