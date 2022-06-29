import re

def parse_string_to_operands(str_example):
    operators = re.split(r'\d+', str_example)
    operands = re.findall(r'\d+', str_example)
    return [op for op in operators if op != ''], [int(op) for op in operands]

    