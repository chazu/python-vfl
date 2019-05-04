from parsimonious.grammar import Grammar

GRAMMAR = Grammar(
    """
    vfsString = (orientation ":")? (superview connection)? view (connection view)* (connection superview)?
    orientation = "H" / "V"
    connection = ("-" predicateList "-") / "-"
    superview = "|"
    view = "[" viewName (predicateListWithParens)? "]"
    predicateListWithParens = "("? predicate ("," predicate)* ")"?
    predicateList = simplePredicate / predicateListWithParens
    simplePredicate = number
    predicate = relation? objectOfPredicate ("@" priority)?
    objectOfPredicate = constant / viewName
    priority = ~"[0-9]+"
    constant = number
    number = ~"[\d]+\.[\d]+"
    viewName = ~"[a-zA-Z]+[a-zA-Z0-9_]*"
    relation = ~"==|>=|<="

    """)
# visualFormatString :
#                    | number
#                    | viewname
#                    | relation
#                    | predicate
#                    | view

# view : "[" viewname "]"
# predicate : relation objectOfPredicate ('@' priority)?

# print(GRAMMAR.parse("|-[someview]-|"))
# print(GRAMMAR.parse("[someView]"))
print(GRAMMAR.parse("[button(>=50)]"))

