from src.Calculator import Calculator
from src.PlusOperator import PlusOperator

def test_plus_operations():
    calc = Calculator([PlusOperator()])
    result = calc.calculate("10+12+14+15")
    assert result == 51
