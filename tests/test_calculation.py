from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('11'), Decimal('2'), add, Decimal('13')),  # Test addition
    (Decimal('20'), Decimal('5'), subtract, Decimal('15')),  # Test subtraction
    (Decimal('100'), Decimal('5'), multiply, Decimal('500')),  # Test multiplication
    (Decimal('100'), Decimal('2'), divide, Decimal('50')),  # Test division
    (Decimal('10.25'), Decimal('10.75'), add, Decimal('21.0')),  # Test addition with decimals
    (Decimal('10.75'), Decimal('1.75'), subtract, Decimal('9.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Test division with decimals
])
def test_calculation_operations(a, b, operation, expected):
    calc = Calculation(a, b, operation)  # Create a Calculation instance with the provided operands and operation.
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_calculation_repr():
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
        