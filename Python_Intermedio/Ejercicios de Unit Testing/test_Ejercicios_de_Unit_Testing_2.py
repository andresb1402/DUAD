import pytest
from Ejercicios_de_Unit_Testing_2 import *


# exercise 3

def test_sum_of_numbers_method():
    numbers_list = [1, 3, 5, 1]
    result = sum_of_numbers_method(numbers_list)
    assert result == 10


def test_sum_of_numbers_method_with_floats():
    numbers_list = [1.15, 3.22, 5.85, 1.71]
    result = sum_of_numbers_method(numbers_list)
    assert result == pytest.approx(11.93)


def test_sum_of_numbers_method_with_negative_numbers():
    numbers_list = [1, -3, 5, 1]
    result = sum_of_numbers_method(numbers_list)
    assert result == 4


# exercise 4

def test_reverse_text():
    sentence = 'Hello people'
    reversed_text = reverse_text(sentence)
    assert reversed_text == "elpoep olleH"


def test_reverse_text_with_reversed_text():
    sentence = 'elpoep olleH'
    reversed_text = reverse_text(sentence)
    assert reversed_text == 'Hello people'


def test_reverse_text_with_empty_input():
    sentence = ''
    reversed_text = reverse_text(sentence)
    assert reversed_text == ''


# exercise 5

def test_upper_and_lower_cases_count():
    upper_cases = 0
    lower_cases = 0
    input_sentence = "My name is Jose Barboza"
    upper_cases, lower_cases = upper_and_lower_cases_count(input_sentence)

    assert upper_cases == 3 and lower_cases == 16


def test_upper_and_lower_cases_count():
    upper_cases = 0
    lower_cases = 0
    input_sentence = "My name is Jose Barboza"
    upper_cases, lower_cases = upper_and_lower_cases_count(input_sentence)

    assert upper_cases == 3 and lower_cases == 16


def test_upper_and_lower_cases_count_including_numbers():
    upper_cases = 0
    lower_cases = 0
    input_sentence = "My 2 name is Jose Barboza 14"
    upper_cases, lower_cases = upper_and_lower_cases_count(input_sentence)

    assert upper_cases == 3 and lower_cases == 16


def test_upper_and_lower_cases_count_with_empty_input():
    upper_cases = 0
    lower_cases = 0
    input_sentence = ''
    upper_cases, lower_cases = upper_and_lower_cases_count(input_sentence)

    assert upper_cases == 0 and lower_cases == 0


# exercise 6

def test_sorting_words():
    test_input = "house-dog-bike-tool-ball-moto"
    sorted_list = sorting_words(test_input)
    assert sorted_list == 'ball-bike-dog-house-moto-tool'


def test_sorting_capitalized_words():
    test_input = "house-Dog-bike-Tool-ball-moto"
    sorted_list = sorting_words(test_input)
    assert sorted_list == 'Dog-Tool-ball-bike-house-moto'


def test_sorting_words_starting_with_the_same_letter():
    test_input = "house-hop-her-high-Hugo-history"
    sorted_list = sorting_words(test_input)
    assert sorted_list == 'Hugo-her-high-history-hop-house'

# exercise 7

def test_prime_numbers():
    input_list = [1, 4, 6, 7, 13, 9, 67]
    prime_numbers_list = prime_numbers(input_list)
    assert prime_numbers_list == [7, 13, 67]


def test_prime_numbers_with_negative_numbers():
    input_list = [1, -4, 6, -7, 13, 9, -67]
    prime_numbers_list = prime_numbers(input_list)
    assert prime_numbers_list == [13]


def test_prime_numbers_without_prime_numbers():
    input_list = [4, 6, 8, 10]
    prime_numbers_list = prime_numbers(input_list)
    assert prime_numbers_list == []