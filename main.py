from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

source = """
sent Name = "Sameer"\\
letter Grade = 'A'\\
logic Student = true\\
logic A = true\\
logic B = false\\
write<Name>\\
write<Grade>\\
write<Student>\\
write<A && B>\\
write<A || B>\\
write<!B>\\
"""

lexer = Lexer(source)
tokens = lexer.tokenize()
parser = Parser(tokens)
tree = parser.parse()
interpreter = Interpreter()
interpreter.execute(tree)