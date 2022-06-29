from src.Parser import convert_to_prefix


class Calculator:
    def __init__(self, operators: list) -> None:
        self.operators = operators

    def calculate(self, line):
        prefix_eq = convert_to_prefix(line)
        return self.execute(prefix_eq)
    
    def execute(self, prefix_equation):
        element = prefix_equation.pop(0)
        if len(prefix_equation) == 0:
            return int(element)
        for op in self.operators:
            if op.can_handle(element):
                res = op.handle(int(prefix_equation.pop(0)), self.execute(prefix_equation))
                return res