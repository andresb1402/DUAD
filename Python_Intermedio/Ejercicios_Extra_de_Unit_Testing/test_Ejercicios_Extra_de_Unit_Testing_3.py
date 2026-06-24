from Ejercicios_Extra_de_Unit_Testing_3 import *
import pytest
from unittest.mock import patch, mock_open


@patch('builtins.open', mock_open(read_data="My name is Jose Barboza"))
def test_read_lines(mock_file):
    result = read_lines("test.txt")
    assert result == ["My name is Jose Barboza"]


@patch('builtins.open')
def test_read_lines_file_not_found(mock_open_generic):
    mock_open_generic.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_lines("test.txt")