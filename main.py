from lexer.lexer import Lexer


source = """
Age <= 20\\
Age >= 10\\
Age == 15\\
Age != 25\\
Age && 10\\
Age || 20\\
!Age\\
"""


lexer = Lexer(source)

tokens = lexer.tokenize()

for token in tokens:
    print(token)