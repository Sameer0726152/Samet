from lexer.lexer import Lexer
from parser.parser import Parser

source = """
logic A = Age > 18 || Age < 10\\
logic B = Age > 18 || Age < 10 && Age != 5\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
tree = parser.parse()

print(tree)