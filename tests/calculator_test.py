"""Testing the Calculator"""
from calculator.main import Calculator

def divide_numbers():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.divide_numbers(0, 5)
    assert result == 5
