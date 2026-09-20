from syntax_tree import Program, Declaration, NumberLiteral, StringLiteral, CharLiteral, BooleanLiteral, If, Identifier, Write, BinaryExpression, Assignment, UnaryExpression
class Environment:
    def __init__(self):
        self.variables = {}

    def define(self, name, value):
        self.variables[name] = value

    def get(self, name):
        if name not in self.variables:
            raise RuntimeError(f"Undefined variable '{name}'")
        return self.variables[name]

    def assign(self, name, value):
        if name not in self.variables:
            raise RuntimeError(f"Undefined variable '{name}'")
        self.variables[name] = value
class Interpreter:
    def __init__(self):
        self.environment = Environment()

    def execute(self, node):
        if isinstance(node, Program):
            for statement in node.statements:
                self.execute(statement)
        elif isinstance(node, Declaration):
            value = self.evaluate(node.value)
            self.environment.define(node.name, value)
        elif isinstance(node, Assignment):
            value = self.evaluate(node.value)
            self.environment.assign(node.name, value)
        elif isinstance(node, Write):
            value = self.evaluate(node.value)
            print(value)
        elif isinstance(node, If):
            condition = self.evaluate(node.condition)
            if condition:
                for statement in node.body:
                    self.execute(statement)
            elif node.else_body is not None:
                for statement in node.else_body:
                    self.execute(statement)

    def evaluate(self, node):
        if isinstance(node, NumberLiteral):
            return node.value
        if isinstance(node, StringLiteral):
            return node.value
        if isinstance(node, CharLiteral):
            return node.value
        if isinstance(node, BooleanLiteral):
            return node.value
        if isinstance(node, Identifier):
            return self.environment.get(node.name)
        if isinstance(node, UnaryExpression):
            operand = self.evaluate(node.operand)
            if node.operator == "!":
                return not operand
            if node.operator == "-":
                return -operand
            raise RuntimeError(f"Unknown unary operator '{node.operator}'")
        if isinstance(node, BinaryExpression):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            operator = node.operator
            if operator == "+":
                return left + right
            if operator == "-":
                return left - right
            if operator == "*":
                return left * right
            if operator == "/":
                return left / right
            if operator == "^":
                return left ** right
            if operator == "<":
                return left < right
            if operator == "<=":
                return left <= right
            if operator == ">":
                return left > right
            if operator == ">=":
                return left >= right
            if operator == "==":
                return left == right
            if operator == "!=":
                return left != right
            if operator == "&&":
                return left and right
            if operator == "||":
                return left or right
            raise RuntimeError(
                f"Unknown binary operator '{operator}'"
            )