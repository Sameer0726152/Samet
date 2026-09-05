class Program:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program(statements={self.statements!r})"

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