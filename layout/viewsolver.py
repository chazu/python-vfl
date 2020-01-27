from vfl.view import View as VFLView

from kiwisolver import (Variable as Var,
                        Solver)


class App:

    def __init__(self):
        self.columns = 50
        self.rows = 50


class ViewSolver:
    """Solver for the space immediately inside this view."""

    def __init__(self, view, width, height):
        # Enclosing view/application
        self.width = width
        self.height = height
        self.view = view
        self._solver = Solver()

        self.constraints = []
        self.variables = {}

        # set up enclosing viewport vars/constraints
        self.add_constraints(self.variable(self.view, "left_side") == 0,
                             self.variable(self.view, "top") == 0,
                             self.variable(self.view, "right_side") == self.width,
                             self.variable(self.view, "bottom") == self.height)

        # Add constraints based on actual contents
        for view in self.view.views:
            view_constraints = [self.constraints_for_connection(x)
                                for x in view.connections]

        # Solve!
        self._solver.updateVariables()

    def add_constraint(self, c):
        self._solver.addConstraint(c)

    def add_constraints(self, *args):
        """Add a series of constraints.
        Note: Implementation here is gross, I know.
        """
        [self._solver.addConstraint(x) for x in args]

    def variable(self, view, name):
        full_name = f"{view.name}_{name}"
        if full_name not in self.variables:
            self.variables[full_name] = Var(full_name)

        return self.variables[full_name]

    def constraints_for_connection(self, cxn):

	# If view is horizontal
	##
        preceding_view = cxn.preceding_view
        following_view = cxn.following_view

        # Implicit connections have no predicates
        # TODO Note that we may have both off-by-one issues here _and_
        # we can probably handle both implicit and explicit connections
        # the same by 1) rolling up predicates where possible into a single value
        # and 2) setting values for implicit connections' predicates to 0
        if cxn.implicit:
	    # For a connection between two things in a horizontal layout

	    #
	    # For a vertical layout, similar but following is below the preceding.

	    # the right side of the preceding view plus the predicate value
	    # equals the left side of the following view.
            self.add_constraint(self.variable(preceding_view, "right_side") ==
                                self.variable(following_view, "left_side"))

            # also the left side of the following view minus the
	    # predicate value equals the right side of the preceding view
            self.add_constraint(self.variable(following_view, "left_side") ==
                                self.variable(preceding_view, "right_side"))

            # In a horizontal layout, top and bottom of both views will be
            # simply the top and bottom of the enclosing view...right?
            # Obviously we're not factoring in margin or padding or anything...
            # yet.
            self.add_constraint(self.variable(following_view, "top") ==
                                self.variable(self.view, "top"))
            self.add_constraint(self.variable(preceding_view, "top") ==
                                self.variable(self.view, "top"))

            self.add_constraint(self.variable(preceding_view, "bottom") ==
                                self.variable(self.view, "bottom"))
            self.add_constraint(self.variable(following_view, "bottom") ==
                                self.variable(self.view, "bottom"))

        else:
            raise "REE We're not handling explicit connections yet"


    def repr(self):
        print("TODO print out all vars, values and constraints")
        # return (f"[[{self.left_side.value()},{self.top.value()}],"
        #         f"[{self.right_side.value()},{self.bottom.value()}]]")
