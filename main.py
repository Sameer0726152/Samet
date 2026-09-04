from lexer.lexer import Lexer


source = """
letter C = 'A'\\
letter X = 'x'\\
"""


lexer = Lexer(source)

tokens = lexer.tokenize()

for token in tokens:
    print(token)