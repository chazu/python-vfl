from parsimonious.grammar import Grammar

GRAMMAR = Grammar(
    """
    vfsString = (orientation ":")? (superview connection)? view (connection view)* (connection superview)?
    orientation = "H" / "V"
    connection = ("-" predicateList "-") / "-"
    superview = "|"
    view = "[" viewName (predicateListWithParens)? "]"
    predicateListWithParens = "(" predicate ("," predicate)* ")"
    predicateList = simplePredicate / predicateListWithParens
    predicate = relation? objectOfPredicate ("@" priority)?
    objectOfPredicate = constant / viewName
    simplePredicate = number
    priority = ~"[0-9]+"
    constant = number
    number = ~"[\d]+\.[\d]+" / ~"[\d]+"
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
print(GRAMMAR.parse("H:|-[someView(>=50)]-|"))

