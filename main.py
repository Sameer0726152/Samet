from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num Age = 20\\
Age = Age + 1\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()

print(tree)