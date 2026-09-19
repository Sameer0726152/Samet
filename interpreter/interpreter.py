from syntax_tree import Program, Declaration, NumberLiteral, Identifier, Write
class Environment:
    def __init__(self):
        self.variables = {}

    def define(self, name, value):
        self.variables[name] = value

    def get(self, name):
        if name not in self.variables:
            raise RuntimeError(f"Undefined variable '{name}'")
        return self.variables[name]

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
        elif isinstance(node, Write):
            value = self.evaluate(node.value)
            print(value)

    def evaluate(self, node):
        if isinstance(node, NumberLiteral):
            return node.value
        if isinstance(node, Identifier):
            return self.environment.get(node.name)