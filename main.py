from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

source = """
num Age = 13\\
if [Age > 18] {write<"Adult">\\}
or {write<"Minor">\\}
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
parser = Parser(tokens)
tree = parser.parse()
interpreter = Interpreter()
interpreter.execute(tree)