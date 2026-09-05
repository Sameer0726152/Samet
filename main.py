from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num Age = 20\\
num Score = 100\\
num Marks = 95\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
print("\nAST:")
parser = Parser(tokens)
ast = parser.parse()
print(ast)