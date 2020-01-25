from kiwisolver import (Variable as Var,
                        Solver)


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

        for c in self.constraints:
            self._solver.addConstraint(c)

        self._solver.updateVariables()

    def repr(self):
        return (f"[[{self.left_side.value()},{self.top.value()}],"
                f"[{self.right_side.value()},{self.bottom.value()}]]")
