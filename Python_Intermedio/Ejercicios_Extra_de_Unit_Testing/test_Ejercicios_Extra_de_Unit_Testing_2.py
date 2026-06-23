from Ejercicios_Extra_de_Unit_Testing_2 import *
import pytest

#Sum
def test_divide_using_valid_numbers():
    num1 = 10
    num2 = 2
    result = divide(num1, num2)
    assert result == pytest.approx(5.0)


def test_divide_using_cero():
    num1 = 10
    num2 = 0
    with pytest.raises(ValueError):
        divide(num1, num2)


def test_divide_using_string():
    num1 = 10
    num2 = 'String'
    with pytest.raises(TypeError):
        divide(num1, num2)