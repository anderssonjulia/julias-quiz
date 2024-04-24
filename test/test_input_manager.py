from unittest.mock import patch

from quiz.input_manager import InputManager
from quiz.question import Question
from quiz.user import User


def test_get_selected_difficulty_easy():
    input_manager = InputManager()

    my_input = "easy"

    def get_input(text=""):
        return my_input

    expected = "easy"

    with patch("builtins.input", side_effect=get_input):
        selected_difficulty = input_manager.get_selected_difficulty()
    assert expected == selected_difficulty


# def test_get_selected_difficulty_invalid():
#     input_manager = InputManager()

#     my_input = "eazy"

#     def get_input(text=""):
#         return my_input

#     expected = None

#     with patch("builtins.input", side_effect=get_input):
#         selected_difficulty = input_manager.get_selected_difficulty()
#     assert expected == selected_difficulty

#     my_input = "easy"

#     expected = "easy"

#     with patch("builtins.input", side_effect=get_input):
#         selected_difficulty = input_manager.get_selected_difficulty()
#     assert expected == selected_difficulty


def test_does_player_want_to_continue_playing_no():

    input_manager = InputManager()

    my_input = "no"

    def get_input(text=""):
        return my_input

    expected = False

    with patch("builtins.input", side_effect=get_input):
        returned = input_manager.does_player_want_to_continue_playing()
    assert expected == returned


def test_does_player_want_to_continue_playing_yes():

    input_manager = InputManager()

    my_input = "yes"

    def get_input(text=""):
        return my_input

    expected = True

    with patch("builtins.input", side_effect=get_input):
        returned = input_manager.does_player_want_to_continue_playing()
    assert expected == returned


def test_get_answer():

    question = Question(question="question?", answer="test_answer", difficulty="easy")

    input_manager = InputManager()

    my_input = "test_answer"

    def get_input(text=""):
        return my_input

    expected_answer = "test_answer"
    expected_result = "Fel"

    with patch("builtins.input", side_effect=get_input):
        input_manager.get_answer(question)
    assert expected_answer == question.answer


def test_get_username():

    user = User(username="Julia")

    input_manager = InputManager()

    my_input = "Julia"

    def get_input(text=""):
        return my_input

    expected = "Julia"

    with patch("builtins.input", side_effect=get_input):
        input_manager.get_username(user)
    assert expected == user.username
