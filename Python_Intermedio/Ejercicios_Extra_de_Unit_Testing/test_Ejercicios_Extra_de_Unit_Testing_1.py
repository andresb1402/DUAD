from Ejercicios_Extra_de_Unit_Testing_1 import *
import pytest

#Sum
def test_sum_with_positive_numbers():
    result = Tests.sum(1, 3, 5, 2)
    assert result == 11


def test_sum_with_negative_numbers():
    result = Tests.sum(-3, -4, -5, -2)
    assert result == -14


def test_sum_with_ceros():
    result = Tests.sum(0, 0, 0, 0)
    assert result == 0


#Average
def test_average_with_positive_numbers():
    result = Tests.average(2, 5, 4, 5)
    assert result == pytest.approx(4)


def test_average_with_negative_numbers():
    result = Tests.average(-3, -4, -5, -2)
    assert result == pytest.approx(-3.5)


def test_average_with_ceros():
    result = Tests.average(0, 0, 0, 0)
    assert result == 0


#Subtract
def test_subtract_with_positive_numbers():
    result = Tests.subtract(15, 6, 4, 1)
    assert result == 4


def test_subtract_with_negative_numbers():
    result = Tests.subtract(-15, -6, -4, -1)
    assert result == -4


def test_subtract_with_ceros():
    result = Tests.subtract(0, 0, 0, 0)
    assert result == 0