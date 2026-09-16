from lexer.lexer import Lexer
from parser.parser import Parser

source = """
logic Same = Age == 20\\
logic Different = Age != 20\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()

print(tree)