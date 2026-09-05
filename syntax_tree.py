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