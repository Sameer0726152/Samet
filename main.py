from lexer.lexer import Lexer


source = """
num Age = 20\\
Age = Age + 1\\
"""


lexer = Lexer(source)

tokens = lexer.tokenize()

for token in tokens:
    print(token)