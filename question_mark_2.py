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
class QuizQuestion:
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


# Ändrade till selected list
def get_random_questions(selected_question_list):
    """docstr"""
    random.seed(21)
    return random.choice(selected_question_list)


class User:
    """docstr"""

    def __init__(self, score=0):
        self.score = score

    def set_username(self):
        """docstr"""
        username = input("Username: ")
        return username

    def add_score(self, score):
        """docstr"""
        score += 1
        return self.score

    def get_score(self):
        """docstr"""
        return self.score


# Ställer frågan och tar in input, vad är skillnaden på denna och QuizQuestion?
# Är det att denna endast har de filtrerade frågorna?
# Nej för det har ju QuestionBoard
class QuestionManager:
    """docstr"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# Har den nuvarande kategorin och dess frågor
class QuestionBoard:
    """docstr"""

    pass


@staticmethod
def create_quiz_question_list_from_json(questions_json_file_path):
    """docstr"""
    # Read the json-file
    questions_json_file_path = Path("questions.json")
    with open(questions_json_file_path, "r") as json_file:
        json_data = json_file.read()

    # Store it in a python list of dicts
    quiz_question_dict_list = json.loads(json_data)

    quiz_question_list = []

    # Create a quiz_question object for each dict in the list
    # Add each quiz_question to the quiz_question_list
    for quiz_question_dict in quiz_question_dict_list:
        quiz_question = QuizQuestion(
            quiz_question_dict["question"],
            quiz_question_dict["answer"],
            quiz_question_dict["difficulty"],
        )
        quiz_question_list.append(quiz_question)

    return quiz_question_list


@staticmethod
def player_choose_difficulty(quiz_question_list):
    """docstr"""
    selected_difficulty = None

    while selected_difficulty is None:
        user_input_choose_difficulty = input(
            "Choose the difficulty of the quiz: (Easy/Medium/Hard) "
        ).lower()
        print()

        # Check if if any of the questions difficulty matches the user input
        # If they are equal, create a variable 'selected_difficulty' and pass the difficulty value
        for quiz_question in quiz_question_list:
            if quiz_question.difficulty.lower() == user_input_choose_difficulty:
                selected_difficulty = quiz_question.difficulty

        # Run this as long as no valid difficulty is passed in
        if selected_difficulty is None:
            print("Choose either easy, medium or hard!")

    return selected_difficulty


@staticmethod
def filter_by_selected_difficulty(selected_difficulty, quiz_question_list):
    """docstr"""
    # Iterate through all the questions
    # Add them to a list if their difficulty matches the chosen one
    filtered_question_list = []
    for quiz_question in quiz_question_list:
        if selected_difficulty == quiz_question.difficulty:
            filtered_question_list.append(quiz_question)

    return filtered_question_list


def game_starts():
    """docstring"""
    continue_playing = True

    print("QUIZ")
    print()

    user = User()

    username = user.set_username()
    score = user.get_score()

    questions_json_file_path = Path("questions.json")
    quiz_question_list = create_quiz_question_list_from_json(questions_json_file_path)

    while continue_playing:
        selected_difficulty = player_choose_difficulty(quiz_question_list)

        filtered_question_list = filter_by_selected_difficulty(
            selected_difficulty, quiz_question_list
        )

        selected_questions_list = copy.deepcopy(filtered_question_list)

        score = run_quiz_round(selected_questions_list, score)

        print("Round is finished " + username + "! Score: " + str(score))

        continue_playing = player_wants_to_continue_playing()

    return selected_questions_list


def run_quiz_round(selected_questions_list, score):
    """docstr"""
    # Looping through the questions and asking for input
    while len(selected_questions_list) > 0:
        # AttributeError: 'list' object has no attribute 'get_random_questions'
        random_question = get_random_questions(selected_questions_list)
        user_answer = input(f"{random_question.question}")

        # Check if the player's answer is correct and remove the question
        if random_question.is_correct(user_answer):
            score += 1
            print("Right answer!!! Score: " + str(score))
        else:
            print("Wrong answer. The correct answer is :", random_question.answer)

        selected_questions_list.remove(random_question)
        print()

    return score


def player_wants_to_continue_playing():
    """docstring"""
    while True:
        yes_or_no = input("Do you want to keep playing? (Yes/No) ").lower()
        print()

        # Check player's answer
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
