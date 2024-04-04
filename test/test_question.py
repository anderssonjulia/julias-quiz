from pathlib import Path
from unittest.mock import patch

from quiz.question import Question
from quiz.question_board import QuestionBoard


def test_constructor():
    question = "question?"
    answer = "test_answer"
    difficulty = "easy"
    question = Question(question, answer, difficulty)
    assert question.question == question
    assert question.answer == answer
    assert question.difficulty == difficulty


def test_create_quiz_question_list_from_json(capsys):
    expected_easy_quiz_question_list_length = 10

    questions_json_file_path = Path("data/questions.json")
    question_list = Question.create_quiz_question_list_from_json(
        questions_json_file_path
    )
    easy_quiz_question_list = QuestionBoard.filter_by_selected_difficulty(
        "Easy", question_list
    )

    assert len(easy_quiz_question_list)
