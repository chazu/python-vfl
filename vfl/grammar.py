from parsimonious.grammar import Grammar

VFL_GRAMMAR = Grammar(
    """
    program = (orientation ":")? (superview connection)? view* (connection view)? (connection superview)?
    orientation = "H" / "V"
    connection = ("-" predicateList "-") / "-"
    superview = "|"
    view = "[" viewName (predicateListWithParens)? "]"
    predicateListWithParens = "(" predicate ("," predicate)* ")"
    predicateList = simplePredicate / predicateListWithParens
    predicate = relation? objectOfPredicate ("@" priority)?
    objectOfPredicate = number / viewName
    simplePredicate = number
    priority = ~"[0-9]+"
    number = ~"[\d]+\.[\d]+" / ~"[\d]+"
    viewName = ~"[a-zA-Z]+[a-zA-Z0-9_]*"
    relation = ~"==|>=|<="
    """)
