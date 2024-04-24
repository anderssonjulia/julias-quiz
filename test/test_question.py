from pathlib import Path
from unittest.mock import patch

from quiz.question import Question


def test_constructor():
    question = "question?"
    answer = "test_answer"
    difficulty = "easy"
    question_example = Question(question, answer, difficulty)
    assert question_example.question == question
    assert question_example.answer == answer
    assert question_example.difficulty == difficulty


def test_is_correct():
    question = Question(question="question?", answer="test_answer", difficulty="easy")

    expected = False

    my_input = "dont know"

    def get_input():
        return my_input

    with patch("builtins.input", side_effect=get_input):
        returned = question.is_correct(my_input)
    assert expected == returned


def test_create_quiz_question_list_from_json():
    expected_easy_quiz_question_list_length = 30

    question_list = Question.create_quiz_question_list_from_json(
        Path("data/questions.json")
    )

    assert len(question_list) == expected_easy_quiz_question_list_length
