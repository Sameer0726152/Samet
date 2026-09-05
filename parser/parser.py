from lexer.tokens import TokenType
from syntax_tree import Program, Declaration, NumberLiteral, BinaryExpression

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
        if type_token.type == TokenType.NUM:
            value = self.parse_expression()
        elif type_token.type == TokenType.SENT:
            value_token = self.expect(TokenType.STRING)
            value = value_token.value
        elif type_token.type == TokenType.LOGIC:
            value_token = self.current()
            if value_token.type == TokenType.TRUE:
                self.advance()
                value = True
            elif value_token.type == TokenType.FALSE:
                self.advance()
                value = False
            else:
                raise SyntaxError(
                    f"Expected TRUE or FALSE "
                    f"at line {value_token.line}, column {value_token.column}"
                )
        elif type_token.type == TokenType.LETTER:
            value_token = self.expect(TokenType.CHAR)
            value = value_token.value
        else:
            raise SyntaxError(
                f"Invalid data type '{type_token.value}' "
                f"at line {type_token.line}, column {type_token.column}"
            )
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
            return NumberLiteral(
                int(token.value)
            )
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