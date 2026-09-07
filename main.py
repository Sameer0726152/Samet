from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num Result = 10 + 5 * 2\\
num Result2 = 100 / 5 + 3\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
print("\nAST:")
parser = Parser(tokens)
ast = parser.parse()
print(ast)