from pathlib import Path

from quiz.user import User
from quiz.input_manager import InputManager
from quiz.question_board import QuestionBoard
from quiz.question import Question

QUESTION_FILE_PATH = Path("data/questions.json")


def print_quiz_header():
    print("QUIZ")
    print()


def start_round(input_manager, user, question_list):

    selected_difficulty = input_manager.get_selected_difficulty()
    question_board = QuestionBoard.filter_by_selected_difficulty(
        selected_difficulty, question_list
    )
    question_board.randomize()

    score = 0
    while len(question_board) > 0:
        question = question_board.pop_question()
        user_question_answer = input_manager.get_answer(question)

        if question.is_correct(user_question_answer):
            score += 1
        else:
            print("Wrong answer. The correct answer is :", question.answer)
        print()

    user.score += score


def main():
    """docstr"""
    # Start game
    print_quiz_header()

    input_manager = InputManager()

    question_list = Question.create_quiz_question_list_from_json(QUESTION_FILE_PATH)

    user = User(username="", score=0)

    user.username = input_manager.get_username(user)

    continue_playing = True

    while continue_playing:
        start_round(input_manager, user, question_list)
        print(f"Score: {user.score}")
        continue_playing = input_manager.does_player_want_to_continue_playing()


if __name__ == "__main__":
    main()