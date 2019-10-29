from vfl.parser import Parser

# result = Parser.parse("H:[viewName(==50@10)]")
result = Parser.parse("[viewName]-50-[anotherView]")
# result = Parser.parse("H:[viewName(30,==anotherView)]")
import pdb; pdb.set_trace()
print(result)
