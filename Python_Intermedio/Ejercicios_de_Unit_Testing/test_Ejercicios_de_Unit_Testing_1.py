# Cree los siguientes unit tests para el algoritmo bubble_sort:

#     Funciona con una lista pequeña.
#     Funciona con una lista grande (de más de 100 elementos.)
#     Funciona con una lista vacía.
#     No funciona con parámetros que no sean una lista.

import pytest
from Ejercicios_de_Unit_Testing_1 import sorting_bubble


def test_sorting_bubble_with_small_list():
    list_input = [3, 4 , 1, 2]
    result = sorting_bubble(list_input)
    assert result == [1, 2, 3, 4]


def test_sorting_bubble_with_large_list():
    large_list = [
    142, 19, 84, 115, 6, 177, 53, 91, 12, 164, 
    33, 105, 50, 128, 71, 199, 2, 88, 145, 62, 
    111, 27, 155, 40, 183, 95, 8, 134, 76, 169, 
    22, 119, 58, 149, 44, 191, 67, 102, 15, 122, 
    81, 3, 158, 98, 137, 29, 174, 49, 108, 85, 
    188, 60, 13, 125, 73, 161, 38, 93, 152, 20, 
    104, 180, 55, 117, 7, 140, 89, 31, 166, 46, 
    131, 64, 196, 11, 147, 80, 172, 52, 97, 25, 
    114, 36, 150, 69, 185, 4, 126, 78, 159, 59, 
    101, 17, 133, 83, 193, 63, 110, 28, 144, 51, 
    168, 41, 121, 92, 179, 14, 136, 70, 153, 35
]
    expected_result = sorted(large_list)
    result = sorting_bubble(large_list)
    assert result == expected_result


def test_sorting_bubble_with_empty_list():
    list_input = []
    result = sorting_bubble(list_input)
    assert result == []


def test_sorting_bubble_without_a_list():
    input_test = 1402
    with pytest.raises(TypeError):
        sorting_bubble(input_test)