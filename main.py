from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num Age = 20\\
sent Name = "Sameer"\\
logic Active = true\\
letter Grade = 'A'\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
for token in tokens:
    print(token)
print("\nAST:")
parser = Parser(tokens)
ast = parser.parse()
print(ast)