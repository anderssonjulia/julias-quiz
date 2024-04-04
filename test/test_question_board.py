import random

from unittest.mock import patch

from quiz.question_board import QuestionBoard


def test_constructor():
    pass


def test___len__(capsys):
    input_list = QuestionBoard()
    input_list.question_list = [1, 2, 3]

    my_input = [1, 2, 3]

    def get_input():
        return len(my_input)

    expected = 3

    with patch("builtins.input", side_effect=get_input):
        QuestionBoard.__len__(input_list)
    assert expected == capsys.readouterr(out="", err="").out


def test_randomize(capsys):
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_input(text=""):
        return random.shuffle(my_input)

    not_expected = "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

    with patch("builtins.input", side_effect=get_input):
        QuestionBoard.randomize(input_list)
    assert not_expected != capsys.readouterr().out


# Räcker det att jag testar pop för en lista
# eller måste jag testa ett objekt som innehåller en lista?
# För det är ju därför jag har metoden från början för att det ska gå för mina objekt
def test_pop_question(capsys):
    input_list = QuestionBoard()
    input_list.question_list = ["1", "2", "3"]

    my_input = ["1", "2", "3"]

    def get_input():
        return my_input.pop(0)

    expected = "2, 3"

    with patch("builtins.input", side_effect=get_input):
        QuestionBoard.pop_question(input_list)
    assert expected == capsys.readouterr().out


def test_append(capsys):
    input_list = ["1", "2", "3"]

    my_input = ["1", "2", "3"]

    def get_input(text=""):
        return my_input.append(4)

    expected = "1, 2, 3, 4"

    with patch("builtins.input", side_effect=get_input):
        QuestionBoard.append(4)
    assert expected == capsys.readouterr().out


def test_filter_by_selected_difficulty():
    pass
