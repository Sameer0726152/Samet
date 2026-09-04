from .tokens import Token, TokenType

class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.keywords = {
            "num": TokenType.NUM,
            "sent": TokenType.SENT,
            "logic": TokenType.LOGIC,
            "letter": TokenType.LETTER,
            "if": TokenType.IF,
            "or": TokenType.OR_KEYWORD,
            "while": TokenType.WHILE,
            "write": TokenType.WRITE,
            "true": TokenType.TRUE,
            "false": TokenType.FALSE
        }
        self.single_char_tokens = {
            "=": TokenType.ASSIGN,
            "!": TokenType.NOT,
            "+": TokenType.PLUS,
            "-": TokenType.MINUS,
            "*": TokenType.MULTIPLY,
            "/": TokenType.DIVIDE,
            "^": TokenType.POWER,
            "<": TokenType.LESS,
            ">": TokenType.GREATER,
            "[": TokenType.LEFT_BRACKET,
            "]": TokenType.RIGHT_BRACKET,
            "{": TokenType.LEFT_BRACE,
            "}": TokenType.RIGHT_BRACE,
            "(": TokenType.LEFT_PAREN,
            ")": TokenType.RIGHT_PAREN,
            "\\": TokenType.STATEMENT_END
        }
        self.multi_char_tokens = {
            "<=": TokenType.LESS_EQUAL,
            ">=": TokenType.GREATER_EQUAL,
            "==": TokenType.EQUAL_EQUAL,
            "!=": TokenType.NOT_EQUAL,
            "&&": TokenType.AND,
            "||": TokenType.OR_OR
        }

    def current(self):
        if self.position >= len(self.source):
            return None
        return self.source[self.position]

    def peek(self):
        if self.position + 1 >= len(self.source):
            return None
        return self.source[self.position + 1]

    def advance(self):
        if self.position >= len(self.source):
            return None
        char = self.source[self.position]
        self.position += 1
        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char

    def tokenize(self):
        tokens = []
        while self.current() is not None:
            char = self.current()
            if char.isspace():
                self.advance()
                continue
            if char.isalpha():
                tokens.append(self.read_word())
                continue
            if char.isdigit():
                tokens.append(self.read_number())
                continue
            if char == '"':
                tokens.append(self.read_string())
                continue
            if self.peek() is not None:
                pair = char + self.peek()
                if pair in self.multi_char_tokens:
                    tokens.append(self.read_multi_char())
                    continue
            if char in self.single_char_tokens:
                tokens.append(self.read_single_char())
                continue
            raise SyntaxError(
                f"Unexpected character '{char}' "
                f"at line {self.line}, column {self.column}"
            )
        tokens.append(
            Token(TokenType.EOF, None, self.line, self.column)
        )
        return tokens

    def read_word(self):
        start_line = self.line
        start_column = self.column
        word = ""
        while self.current() is not None:
            char = self.current()
            if char.isalpha() or char.isdigit() or char == "_":
                word += self.advance()
            else:
                break
        if word in self.keywords:
            token_type = self.keywords[word]
            return Token(
                token_type,
                word,
                start_line,
                start_column
            )
        if not word[0].isupper():
            raise SyntaxError(
                f"Identifier '{word}' must start with a capital letter "
                f"at line {start_line}, column {start_column}"
            )
        return Token(
            TokenType.IDENTIFIER,
            word,
            start_line,
            start_column
        )

    def read_number(self):
        start_line = self.line
        start_column = self.column
        number = ""
        while self.current() is not None:
            char = self.current()
            if char.isdigit():
                number += self.advance()
            else:
                break
        return Token(
            TokenType.NUMBER,
            number,
            start_line,
            start_column
        )

    def read_single_char(self):
        line = self.line
        column = self.column
        char = self.advance()
        token_type = self.single_char_tokens[char]
        return Token(
            token_type,
            char,
            line,
            column
        )

    def read_multi_char(self):
        line = self.line
        column = self.column
        first = self.advance()
        second = self.advance()
        operator = first + second
        token_type = self.multi_char_tokens[operator]
        return Token(
            token_type,
            operator,
            line,
            column
        )

    def read_string(self):
        start_line = self.line
        start_column = self.column
        self.advance()  
        string = ""
        while self.current() is not None:
            char = self.current()
            if char == '"':
                self.advance() 
                return Token(
                    TokenType.STRING,
                    string,
                    start_line,
                    start_column
                )
            if char == "\n":
                raise SyntaxError(
                    f"Unterminated string at line "
                    f"{start_line}, column {start_column}"
                )
            string += self.advance()
        raise SyntaxError(
            f"Unterminated string at line "
            f"{start_line}, column {start_column}"
        )