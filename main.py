from lexer.lexer import Lexer


source = """
sent Name = "Sam"\\
write<"Hello World">\\
"""


lexer = Lexer(source)

tokens = lexer.tokenize()

for token in tokens:
    print(token)