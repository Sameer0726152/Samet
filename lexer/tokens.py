from enum import Enum, auto

class TokenType(Enum):
    NUM = auto()
    SENT = auto()
    LOGIC = auto()
    LETTER = auto()
    IF = auto()
    OR_KEYWORD = auto()
    WHILE = auto()
    WRITE = auto()
    TRUE = auto()
    FALSE = auto()
    NUMBER = auto()
    STRING = auto()
    CHAR = auto()
    IDENTIFIER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    ASSIGN = auto()
    LESS = auto()
    GREATER = auto()
    LESS_EQUAL = auto()
    GREATER_EQUAL = auto()
    EQUAL_EQUAL = auto()
    NOT_EQUAL = auto()
    AND = auto()
    OR_OR = auto()
    NOT = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    STATEMENT_END = auto()
    EOF = auto()

class Token:
    def __init__(self, token_type, value, line, column):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column
        
    def __repr__(self):
        return (
            f"Token("
            f"type={self.type.name}, "
            f"value={self.value!r}, "
            f"line={self.line}, "
            f"column={self.column}"
            f")"
        )