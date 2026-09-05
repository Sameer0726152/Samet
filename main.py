from lexer.lexer import Lexer


source = """
# This is a comment
num Age = 20\\ # Age declaration
Age = Age + 1\\ # Increase age
write<Age>\\
"""


lexer = Lexer(source)

tokens = lexer.tokenize()

for token in tokens:
    print(token)