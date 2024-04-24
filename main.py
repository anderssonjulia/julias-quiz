"Main"

from pathlib import Path

from quiz.quiz import start_quiz
from quiz.input_manager import InputManager
from quiz.question import Question
from quiz.user import User

QUESTION_FILE_PATH = Path("data/questions.json")

if __name__ == "__main__":

    user = User(username="", score=0)

    input_manager = InputManager()

    question_list = Question.create_quiz_question_list_from_json(QUESTION_FILE_PATH)

    start_quiz(input_manager, question_list, user)
