from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num A = 2 + 3 * 4\\
num B = (2 + 3) * 4\\
num C = 2 * (3 + 4)\\
num D = ((2 + 3) * 4)\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
print("\nAST:")
parser = Parser(tokens)
ast = parser.parse()
print(ast)