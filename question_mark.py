"""myquiz.py is a python file that allows you to do a quiz with 
three different difficulties. First you enter your username 
and then choose preferred difficulty, each containing 10 questions. 
Each correct answer gives you a point and after the 10 questions are done, 
you can choose to either stop or keep playing. If you continue playing 
you can choose a new difficulty, including the previous. 
Your score is saved from previous rounds, until you exit the quiz."""

import json
import random
import copy
from pathlib import Path


# Get questions from the json-file
class QuizQuestion():
    """docstring"""
    def __init__(self, question, answer, difficulty):
        """docstring"""
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def display_question(self):
        """Dispay the question."""
        print(f"Question: {self.question}")

    def display_answer(self):
        """Display the answer."""
        print(f"Answer: {self.answer}")

    def is_correct(self, user_answer):
        """Check if the user's input is the correct answer."""
        return user_answer.lower() == self.answer.lower()

    def get_random_questions(quiz_question_list):
        random.seed(21)
        return random.choice(quiz_question_list)

    questions_json_file_path = Path("questions.json")

@staticmethod
def create_quiz_question_list_from_json(questions_json_file_path):
    with open(questions_json_file_path, "r") as json_file:
        json_data = json_file.read()

    quiz_question_dict_list = json.loads(json_data)

    quiz_question_list = []

    for quiz_question_dict in quiz_question_dict_list:
        quiz_question = QuizQuestion(
            quiz_question_dict["question"], quiz_question_dict["answer"], quiz_question_dict["difficulty"]
        )
        quiz_question_list.append(quiz_question)

    return quiz_question_list

@staticmethod
def player_choose_difficulty(quiz_question_list):
    selected_difficulty = None

    while selected_difficulty is None:
        user_input_choose_difficulty = input(
            "Choose the difficulty of the quiz: (Easy/Medium/Hard) "
        ).lower()
        print()

        for difficulty in quiz_question_list:
            if difficulty.name.lower() == user_input_choose_difficulty:
                selected_difficulty = difficulty

        if selected_difficulty is None:
            print("Choose either easy, medium or hard!")
        
    return selected_difficulty

@staticmethod
def filter_by_selected_difficulty(selected_difficulty, quiz_question_list):
    filtered_question_list = []
    for quiz_question in quiz_question_list:
        if selected_difficulty == quiz_question.difficulty:
            filtered_question_list.append(quiz_question)

    return filtered_question_list


def game_starts():
    """docstring"""
    continue_playing = True

    total_score = 0

    user_input_name = get_user_input_name()

    questions_json_file_path = Path("questions.json")
    quiz_question_list = create_quiz_question_list_from_json(questions_json_file_path)

    selected_difficulty = player_choose_difficulty(quiz_question_list)

    filtered_question_list = filter_by_selected_difficulty(selected_difficulty, quiz_question_list)

    while continue_playing:

        selected_difficulty = filter_by_selected_difficulty(quiz_question_list)

        selected_difficulty_copy = copy.deepcopy(selected_difficulty)

        # Select question, get answer and get point
        total_score += run_quiz_round(selected_difficulty_copy, total_score)

        print("Round is finished " + user_input_name + "! Score: " + str(total_score))

        # Keep playing or not
        continue_playing = player_wants_to_continue_playing()


def get_user_input_name():
    """docstr"""
    print("QUIZ")
    print()
    user_input_name = input("Username: ")

    return user_input_name


def run_quiz_round(selected_difficulty_copy, total_score):
    """docstr"""
    round_score = 0

    while selected_difficulty_copy.questions:
        random_question = selected_difficulty_copy.get_random_questions()
        user_question_answer = input(f"{random_question.question}")

        if random_question.is_correct(user_question_answer):
            round_score = round_score + 1
            print("Right answer!!! Score: " + str(total_score + round_score))
        else:
            print("Wrong answer. The correct answer is :", random_question.answer)

        selected_difficulty_copy.questions.remove(random_question)
        print()

    return round_score


def player_wants_to_continue_playing():
    """docstring"""
    while True:
        yes_or_no = input("Do you want to keep playing? (Yes/No) ").lower()
        print()

        if yes_or_no == "yes":
            return True
        if yes_or_no == "no":
            return False
        if yes_or_no not in ("yes", "no"):
            print("Choose either yes or no: ")


def main():
    """docstring"""
    # Start game
    game_starts()


if __name__ == "__main__":
    main()













# class QuizQuestion():
#     """docstring"""
#     def __init__(self, question, answer, difficulty, name, all_questions):
#         """docstring"""
#         self.question = question
#         self.answer = answer
#         self.difficulty = difficulty
#         # self.name = name
#         # self.all_questions = []

#         # for question_data in all_questions:
#         #     loop = QuizQuestion(
#         #         question=question_data["question"], answer=question_data["answer"]
#         #     )
#         #     self.questions.append(loop)

#     def display_question(self):
#         """Dispay the question."""
#         print(f"Question: {self.question}")

#     def display_answer(self):
#         """Display the answer."""
#         print(f"Answer: {self.answer}")

#     def is_correct(self, user_answer):
#         """Check if the user's input is the correct answer."""
#         return user_answer.lower() == self.answer.lower()
    
#     # def get_random_questions(self):
#     #     """The questions appear in a random but set order."""
#     #     random.seed(21)
#     #     return random.choice(self.all_questions)

#     # def get_all_questions(self):
#     #     """Get all questions in difficulty."""
#     #     return self.all_questions


# def get_difficulty_list(json_file_path):
#     """docstring"""

#     # Get Difficulties dict from json file
#     with open(json_file_path, "r", encoding="utf-8") as json_file:
#         json_data = json_file.read()

#     data = json.loads(json_data)

#     # Create Difficulty objects
#     difficulty_list = []

#     for difficulty_data in data["difficulties"]:
#         difficulty = Difficulty(
#             name=difficulty_data["name"], questions=difficulty_data["questions"]
#         )
#         difficulty_list.append(difficulty)

#     return difficulty_list


# class QuizQuestion():
#     """docstring"""
#     def __init__(self, question, answer, difficulty):
#         """docstring"""
#         self.question = question
#         self.answer = answer
#         self.difficulty = difficulty

#     def display_question(self):
#         """Dispay the question."""
#         print(f"Question: {self.question}")

#     def display_answer(self):
#         """Display the answer."""
#         print(f"Answer: {self.answer}")

#     def is_correct(self, user_answer):
#         """Check if the user's input is the correct answer."""
#         return user_answer.lower() == self.answer.lower()

#     questions_json_file_path = Path("questions.json")

#     @staticmethod
#     def create_quiz_question_list_from_json(questions_json_file_path):
#         with open(questions_json_file_path, "r") as json_file:
#             json_data = json_file.read()

#         quiz_question_dict_list = json.loads(json_data)
        
#         quiz_question_list = []

#         for quiz_question_dict in quiz_question_dict_list:
#             quiz_question = QuizQuestion(
#                 quiz_question_dict["question"], quiz_question_dict["answer"], quiz_question_dict["difficulty"]
#             )
#             quiz_question_list.append(quiz_question)

#         return quiz_question_list

#     @staticmethod
#     def filter_by_difficulty(difficulty, quiz_question_list):
#         filtered_question_list = []
#         for quiz_question in quiz_question_list:
#             if difficulty == quiz_question.difficulty:
#                 filtered_question_list.append(quiz_question)

#         return filtered_question_list


# class User:
#     """docstring"""
#     def __init__(self, username):
#         """docstring"""
#         self.username = username
#         self.scores = []

#         User.num_users += 1

#     def get_username(self):
#         """docstring"""
#         return self.username
    
#     def add_score(self, score):
#         self.scores.append(score)

#     def get_score(self):
#         """docstring"""
#         return self.scores
    
#     def get_rank(self):
#         """docstring"""
#         return self.rank
    
# def leaderboard(score):
#     pass
