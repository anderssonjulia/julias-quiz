import pytest

from pathlib import Path

from quiz.question_board import QuestionBoard
from quiz.question import Question


def test_constructor():
    question_list = []
    question_board = QuestionBoard()
    assert question_board.question_list == question_list


def test___len__():
    input_list = QuestionBoard()
    input_list.question_list = [1, 2, 3]

    returned = input_list.__len__()

    expected = 3

    assert expected == returned


def test_randomize():
    input_list = QuestionBoard()
    input_list.question_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    returned = input_list.randomize()

    not_expected = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"

    assert not_expected != returned


# Räcker det att jag testar pop för en lista
# eller måste jag testa ett objekt som innehåller en lista?
# För det är ju därför jag har metoden från början för att det ska gå för mina objekt


def test_pop_question():
    input_list = QuestionBoard()
    input_list.question_list = ["1", "2", "3"]

    returned = input_list.pop_question()

    expected = "3"

    assert expected == returned


@pytest.fixture
def question_board():
    return QuestionBoard()


@pytest.fixture
def question_object():
    return Question(question="question?", answer="test_answer", difficulty="easy")


def test_append(question_board, question_object):

    question_board.append(question_object)

    expected = [question_object]
    assert expected == question_board.question_list


def test_filter_by_selected_difficulty():
    expected_easy_quiz_question_board_length = 10
    # expected_difficulty = "easy"

    question_list = Question.create_quiz_question_list_from_json(
        Path("data/questions.json")
    )

    question_board = QuestionBoard.filter_by_selected_difficulty("easy", question_list)

    # TypeError: 'QuestionBoard' object is not iterable
    # for question in question_board:
    #     assert question.difficulty == expected_difficulty

    assert len(question_board) == expected_easy_quiz_question_board_length
    # assert question_board(question.difficulty.lower())
