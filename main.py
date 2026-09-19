from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

source = """
num A = 20\\
write<A + 5>\\
write<A - 5>\\
write<A * 2>\\
write<A / 2>\\
write<A ^ 2>\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
parser = Parser(tokens)
tree = parser.parse()
interpreter = Interpreter()
interpreter.execute(tree)