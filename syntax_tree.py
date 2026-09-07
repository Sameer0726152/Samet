class Program:
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        return f"Program(statements={self.statements!r})"
class NumberLiteral:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"NumberLiteral(value={self.value!r})"
class StringLiteral:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"StringLiteral(value={self.value!r})"
class CharLiteral:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"CharLiteral(value={self.value!r})"
class BooleanLiteral:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"BooleanLiteral(value={self.value!r})"
class Identifier:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Identifier(name={self.name!r})"
class BinaryExpression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return (
            f"BinaryExpression("
            f"left={self.left!r}, "
            f"operator={self.operator!r}, "
            f"right={self.right!r}"
            f")"
        )
class UnaryExpression:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    def __repr__(self):
        return (
            f"UnaryExpression("
            f"operator={self.operator!r}, "
            f"operand={self.operand!r}"
            f")"
        )
class Declaration:
    def __init__(self, data_type, name, value):
        self.data_type = data_type
        self.name = name
        self.value = value
    def __repr__(self):
        return (
            f"Declaration("
            f"data_type={self.data_type!r}, "
            f"name={self.name!r}, "
            f"value={self.value!r}"
            f")"
        )