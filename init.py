from vfl.parser import Parser

# result = Parser.parse("H:[viewName(==50@10)]")
# result = Parser.parse("[viewName(>=50,<=100)]-50-[anotherView]")
# result = Parser.parse("H:[viewName(30,==anotherView)]")
result = Parser.parse("|-50-[purpleBox]-50-|")

print(result)
