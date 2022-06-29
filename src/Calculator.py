from src.PlusOperator import PlusOperator
from src.MultiplyOperator import MultiplyOperator
from src.Parser import parse_string_to_operands


class Calculator:
    def __init__(self, operators: list) -> None:
        self.operators = operators

    def calculate(self, line):
        operators, operands = parse_string_to_operands(line)
        return self.execute(operators, operands)
    
    def execute(self, operators, operands):
        if len(operators) == 0:
            return operands[0]
        operator = operators[0]
        operand = operands[0]

        for op in self.operators:
            if op.can_handle(operator):
                res = op.handle(operand, self.execute(operators[1:], operands[1:]))
                print(res, operand, operator)
                return res


if __name__ == '__main__':
    operators = [PlusOperator(), MultiplyOperator()]
    print(f"Enter your equation without spaces. Supported operators: {operators}")
    print("To exit, type exit.")
    calc = Calculator(operators)
    while True:
        new_line = input()
        if new_line.lower() == 'exit':
            exit(0)
        result = calc.calculate(new_line)
        print(result)