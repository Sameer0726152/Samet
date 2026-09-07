from lexer.tokens import TokenType
from syntax_tree import Program, Declaration, NumberLiteral, StringLiteral, CharLiteral, BooleanLiteral, Identifier, BinaryExpression

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
        value = self.parse_expression()
        self.expect(TokenType.STATEMENT_END)
        return Declaration(
            type_token.value,
            name_token.value,
            value
        )

    def parse(self):
        statements = []
        while self.current().type != TokenType.EOF:
            statements.append(self.parse_declaration())
        return Program(statements)

    def parse_primary(self):
        token = self.current()
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberLiteral(int(token.value))
        if token.type == TokenType.STRING:
            self.advance()
            return StringLiteral(token.value)
        if token.type == TokenType.CHAR:
            self.advance()
            return CharLiteral(token.value)
        if token.type == TokenType.TRUE:
            self.advance()
            return BooleanLiteral(True)
        if token.type == TokenType.FALSE:
            self.advance()
            return BooleanLiteral(False)
        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return Identifier(token.value)
        raise SyntaxError(
            f"Expected expression, "
            f"but found {token.type.name} "
            f"at line {token.line}, column {token.column}"
        )

    def parse_term(self):
        left = self.parse_primary()
        while self.current().type in (
            TokenType.PLUS,
            TokenType.MINUS
        ):
            operator_token = self.advance()
            right = self.parse_primary()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_expression(self):
        return self.parse_term()