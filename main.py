from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

source = """
num Age = 20\\
write<Age > 18>\\
write<Age == 20>\\
write<!(Age > 18)>\\
write<Age > 18 && Age < 60>\\
write<Age < 10 || Age > 18>\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
parser = Parser(tokens)
tree = parser.parse()
interpreter = Interpreter()
interpreter.execute(tree)