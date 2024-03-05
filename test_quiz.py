import pytest
from unittest.mock import patch
from myquiz import (
    get_user_input_choose_difficulty,
    get_user_imput_name,
    get_CONTINUE_PLAYING,
)


def test_get_user_input_choose_difficulty():
    test_cases = [("easy", "easy"), ("medium", "medium"), ("hard", "hard")]

    for input_value, expected_result in test_cases:
        with patch("builtins.input", return_value=input_value):
            result = get_user_input_choose_difficulty()
            assert result == expected_result


def test_get_user_input_name():
    with patch("builtints.input", return_value="Julia"):
        result = get_user_imput_name()

    assert result == "Julia"


def test_get_CONTINUE_PLAYING():
    test_cases = [("yes", "yes"), ("no", "no")]

    for input_value, expected_result in test_cases:
        with patch("builtins.input", return_value=input_value):
            result = get_CONTINUE_PLAYING()
            assert result == expected_result

# Reformat the code into a fixture
