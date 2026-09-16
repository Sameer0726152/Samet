from lexer.lexer import Lexer
from parser.parser import Parser

source = """
logic Adult = Age > 18 && Age < 60\\
logic Same = Age == 20 && Age != 30\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()

print(tree)