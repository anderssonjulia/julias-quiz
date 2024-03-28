# """myquiz.py is a python file that allows you to do a quiz with
# three different difficulties. First you enter your username
# and then choose preferred difficulty, each containing 10 questions.
# Each correct answer gives you a point and after the 10 questions are done,
# you can choose to either stop or keep playing. If you continue playing
# you can choose a new difficulty, including the previous.
# Your score is saved from previous rounds, until you exit the quiz."""

import random
from pathlib import Path

from quiz.user import User
from quiz.input_manager import InputManager
from quiz.question_board import QuestionBoard
from quiz.question import Question

# def game_starts():
#     """docstr"""


#     ################################
#     continue_playing = True

#     print("QUIZ")
#     print()

#     user = User()

#     username = user.set_username()

#     questions_json_file_path = Path("questions.json")
#     quiz_question_list = create_quiz_question_list_from_json(questions_json_file_path)

#     while continue_playing:
#         selected_difficulty = player_choose_difficulty(quiz_question_list)

#         selected_question = filter_by_selected_difficulty(
#             selected_difficulty, quiz_question_list
#         )

#         score = run_quiz_round(selected_question, score)

#         print("Round is finished " + username + "! Score: " + str(score))

#         continue_playing = player_wants_to_continue_playing()

#     return selected_question


# def run_quiz_round(selected_question_list, score):
#     """docstr"""

#     question_manager = QuestionManager()

#     while len(selected_question_list) > 0:

#         random_question = question_manager.get_random_question(selected_question_list)
#         # Looping through the questions and asking for input
#         user_answer, random_question = question_manager.get_answer_input(
#             selected_question_list
#         )
#         # Check if the player's answer is correct and remove the question
#         selected_question_list, score = question_manager.check_answer(
#             random_question, selected_question_list, user_answer, score
#         )

#     return score


# def player_wants_to_continue_playing():
#     """docstr"""
#     while True:
#         yes_or_no = input("Do you want to keep playing? (Yes/No) ").lower()
#         print()

#         # Check player's answer
#         if yes_or_no == "yes":
#             return True
#         if yes_or_no == "no":
#             return False
#         if yes_or_no not in ("yes", "no"):
#             print("Choose either yes or no: ")

QUESTION_FILE_PATH = Path("questions.json")


def main():
    """docstr"""
    # Start game

    input_manager = InputManager()

    question_list = Question.create_quiz_question_list_from_json(QUESTION_FILE_PATH)

    user = User()
    input_manager.set_user_name(user)
    input_manager.get_question_board()

    input_manager.start_quiz()

    question_board = QuestionBoard()


if __name__ == "__main__":
    main()

# Jag fattar inte riktigt skillnaden mellan selected_questions och
# selected_questions list. Selected_questions_list ska ju vara en lista
# av seleced_questions, men den i sin tur har ju attributes som är questions
# Så jag kanske har en extra nivå, men sen vill jag ju ha en lista av dicts
# Precis som i quiz_question och quiz_question_list
# Kan man göra QuestionBoard till en child class av QuizQuestion?
# Eller tvärt om?
