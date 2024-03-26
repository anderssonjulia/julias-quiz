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


# Classes for the json-file
class Question:
    """Class documentation for Question."""

    def __init__(self, question, answer):
        """Constructor documentation."""
        self.question = question
        self.answer = answer

    def display_question(self):
        """Dispay the question."""
        return {self.question}

    def display_answer(self):
        """Display the answer."""
        return {self.answer}

    def is_correct(self, user_answer):
        """Check if the user's input is the correct answer."""
        return user_answer.lower() == self.answer.lower()


class Difficulty:
    """Class documentation for difficulty."""

    def __init__(self, name, questions):
        """Constructor documentation."""
        self.name = name
        self.questions = []

        for question_data in questions:
            ask = Question(
                question=question_data["question"], answer=question_data["answer"]
            )
            self.questions.append(ask)

    def get_random_questions(self):
        """The questions appear in a random but set order."""
        random.seed(21)
        return random.choice(self.questions)

    def get_all_questions(self):
        """Get all questions in difficulty."""
        return self.questions


def game_starts():
    """docstring"""
    continue_playing = True

    total_score = 0
    json_file_path = "myquiz.json"
    difficulty_list = get_difficulty_list(json_file_path)

    user_input_name = get_user_input_name()

    while continue_playing:

        selected_difficulty = player_choose_difficulty(difficulty_list)

        selected_difficulty_copy = copy.deepcopy(selected_difficulty)

        # Select question, get answer and get point
        total_score += run_quiz_round(selected_difficulty_copy, total_score)

        print("Round is finished " + user_input_name + "! Score: " + str(total_score))

        # Keep playing or not
        continue_playing = player_wants_to_continue_playing()


def get_difficulty_list(json_file_path):
    """docstring"""

    # Get Difficulties dict from json file
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        json_data = json_file.read()

    data = json.loads(json_data)

    # Create Difficulty objects
    difficulty_list = []

    for difficulty_data in data["difficulties"]:
        difficulty = Difficulty(
            name=difficulty_data["name"], questions=difficulty_data["questions"]
        )
        difficulty_list.append(difficulty)

    return difficulty_list


def get_user_input_name():
    """docstr"""
    print("WELCOME TO QUIZ")
    print()
    user_input_name = input("Username: ")

    return user_input_name 


def player_choose_difficulty(difficulty_list):
    """docstr"""
    selected_difficulty = None

    while selected_difficulty is None:
        user_input_choose_difficulty = input(
            "Choose the difficulty of the quiz: (Easy/Medium/Hard) "
        ).lower()
        print()

        for difficulty in difficulty_list:
            if difficulty.name.lower() == user_input_choose_difficulty:
                selected_difficulty = difficulty

        if selected_difficulty is None:
            print("Choose either easy, medium or hard!")

    return selected_difficulty


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
