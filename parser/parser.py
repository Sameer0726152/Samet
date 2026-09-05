from lexer.tokens import TokenType
from syntax_tree import Program, Declaration

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position >= len(self.tokens):
            return None
        return self.tokens[self.position]

    def advance(self):
        if self.position >= len(self.tokens):
            return None
        token = self.tokens[self.position]
        self.position += 1
        return token

    def expect(self, token_type):
        token = self.current()
        if token is None:
            raise SyntaxError(
                f"Expected {token_type.name}, but reached end of input"
            )
        if token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type.name}, "
                f"but found {token.type.name} "
                f"at line {token.line}, column {token.column}"
            )
        return self.advance()

    def parse_declaration(self):
        type_token = self.advance()
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.ASSIGN)
        value_token = self.expect(TokenType.NUMBER)
        self.expect(TokenType.STATEMENT_END)
        return Declaration(
            type_token.value,
            name_token.value,
            int(value_token.value)
        )

    def parse(self):
        statements = []
        while self.current().type != TokenType.EOF:
            statements.append(self.parse_declaration())
        return Program(statements)