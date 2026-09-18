from lexer.tokens import TokenType
from syntax_tree import Program, Declaration, NumberLiteral, StringLiteral, If, CharLiteral, BooleanLiteral, Identifier, UnaryExpression, BinaryExpression, Assignment, Write

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        if self.position >= len(self.tokens):
            return None
        return self.tokens[self.position]

    def peek(self):
        if self.position + 1 >= len(self.tokens):
            return None
        return self.tokens[self.position + 1]

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
            statements.append(self.parse_statement())
        return Program(statements)

    def parse_block(self):
        self.expect(TokenType.LEFT_BRACE)
        statements = []
        while (
            self.current().type != TokenType.RIGHT_BRACE
            and self.current().type != TokenType.EOF
        ):
            statements.append(self.parse_statement())
        self.expect(TokenType.RIGHT_BRACE)

        return statements

    def parse_statement(self):
        if self.current().type in (
            TokenType.NUM,
            TokenType.SENT,
            TokenType.LOGIC,
            TokenType.LETTER
        ):
            return self.parse_declaration()
        elif self.current().type == TokenType.IDENTIFIER:
            return self.parse_assignment()
        elif self.current().type == TokenType.WRITE:
            return self.parse_write()
        elif self.current().type == TokenType.IF:
            return self.parse_if()
        else:
            token = self.current()
            raise SyntaxError(
                f"Unexpected token {token.type.name} "
                f"at line {token.line}, column {token.column}"
            )

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
        if token.type == TokenType.LEFT_PAREN:
            self.advance()
            expression = self.parse_expression()
            self.expect(TokenType.RIGHT_PAREN)
            return expression
        raise SyntaxError(
            f"Expected expression, "
            f"but found {token.type.name} "
            f"at line {token.line}, column {token.column}"
        )

    def parse_term(self):
        left = self.parse_factor()
        while self.current().type in (
            TokenType.PLUS,
            TokenType.MINUS
        ):
            operator_token = self.advance()
            right = self.parse_factor()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_factor(self):
        left = self.parse_power()
        while self.current().type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE
        ):
            operator_token = self.advance()
            right = self.parse_power()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_power(self):
        left = self.parse_unary()
        while self.current().type == TokenType.POWER:
            operator_token = self.advance()
            right = self.parse_unary()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_unary(self):
        token = self.current()
        if token.type == TokenType.NOT:
            self.advance()
            operand = self.parse_unary()
            return UnaryExpression(
                token.value,
                operand
            )
        if token.type == TokenType.MINUS:
            self.advance()
            operand = self.parse_unary()
            return UnaryExpression(
                token.value,
                operand
            )
        return self.parse_primary()

    def parse_comparison(self):
        left = self.parse_term()
        while self.current().type in (
            TokenType.LESS,
            TokenType.LESS_EQUAL,
            TokenType.GREATER,
            TokenType.GREATER_EQUAL
        ):
            if (
                self.current().type == TokenType.GREATER
                and self.peek().type == TokenType.STATEMENT_END
            ):
                break
            operator_token = self.advance()
            right = self.parse_term()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )

        return left

    def parse_equality(self):
        left = self.parse_comparison()
        while self.current().type in (
            TokenType.EQUAL_EQUAL,
            TokenType.NOT_EQUAL
        ):
            operator_token = self.advance()
            right = self.parse_comparison()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_logical_and(self):
        left = self.parse_equality()
        while self.current().type == TokenType.AND:
            operator_token = self.advance()
            right = self.parse_equality()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_logical_or(self):
        left = self.parse_logical_and()
        while self.current().type == TokenType.OR_OR:
            operator_token = self.advance()
            right = self.parse_logical_and()
            left = BinaryExpression(
                left,
                operator_token.value,
                right
            )
        return left

    def parse_assignment(self):
        name_token = self.expect(TokenType.IDENTIFIER)
        self.expect(TokenType.ASSIGN)
        value = self.parse_expression()
        self.expect(TokenType.STATEMENT_END)
        return Assignment(
            name_token.value,
            value
        )

    def parse_write(self):
        self.expect(TokenType.WRITE)
        self.expect(TokenType.LESS)
        value = self.parse_expression()
        self.expect(TokenType.GREATER)
        self.expect(TokenType.STATEMENT_END)
        return Write(value)

    def parse_if(self):
        self.expect(TokenType.IF)
        self.expect(TokenType.LEFT_BRACKET)
        condition = self.parse_expression()
        self.expect(TokenType.RIGHT_BRACKET)
        body = self.parse_block()
        else_body = None
        if self.current().type == TokenType.OR_KEYWORD:
            self.expect(TokenType.OR_KEYWORD)
            else_body = self.parse_block()
        return If(
            condition,
            body,
            else_body
        )

    def parse_expression(self):
        return self.parse_logical_or()