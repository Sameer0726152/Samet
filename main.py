from lexer.lexer import Lexer
from parser.parser import Parser

source = """
num Age = 20\\
write<Age>\\
write<Age + 10>\\
write<Age > 18>\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
parser = Parser(tokens)
tree = parser.parse()
print(tree)