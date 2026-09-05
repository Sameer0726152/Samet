from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num Age = 20 + 5\\
num Score = 100 - 25\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
print("\nAST:")
parser = Parser(tokens)
ast = parser.parse()
print(ast)