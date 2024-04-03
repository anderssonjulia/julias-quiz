import random

from unittest.mock import patch

from quiz.question_board import QuestionBoard


def test_constructor():
    pass

def test___len__():
    pass

def test_randomize(capsys):
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_input(text=""):
        return my_input.randomize(input_list)
    
    expected = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

    with patch("builtins.input", side_effect=get_input):
        QuestionBoard.randomize()
    assert expected != capsys.readouterr().out

def test_pop_question():
    pass

def test_append():
    pass

def test_filter_by_selected_difficulty():
    pass