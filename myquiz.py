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
        print(f"Question: {self.question}")

    def display_answer(self):
        """Display the answer."""
        print(f"Answer: {self.answer}")

    def is_correct(self, user_answer):
        """Check if the user's input is the correct answer."""
        return user_answer.lower() == self.answer.lower()


class Category:
    """Class documentation for Category."""

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
        """Get all questions in category."""
        return self.questions


def get_category_list(json_file_path):
    """docstring"""

    # Get Categories dict from json file
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        json_data = json_file.read()

    data = json.loads(json_data)

    # Create Catergories objects
    category_list = []

    for category_data in data["categories"]:
        category = Category(
            name=category_data["name"], questions=category_data["questions"]
        )
        category_list.append(category)

    return category_list


def startup():
    """docstr"""
    print("QUIZ")
    print()
    user_input_name = input("Username: ")

    return user_input_name


def player_choose_category(category_list):
    """docstr"""
    selected_category = None

    while selected_category is None:
        user_input_choose_difficulty = input(
            "Choose the difficulty of the quiz: (Easy/Medium/Hard) "
        ).lower()
        print()

        for category in category_list:
            if category.name.lower() == user_input_choose_difficulty:
                selected_category = category

        if selected_category is None:
            print("Choose either easy, medium or hard!")

    return selected_category


def question_and_answer(selected_category_copy, total_score):
    """docstr"""
    round_score = 0

    while selected_category_copy.questions:
        random_question = selected_category_copy.get_random_questions()
        user_question_answer = input(f"{random_question.question}")

        if random_question.is_correct(user_question_answer):
            round_score = round_score + 1
            print("Right answer!!! Score: " + str(total_score + round_score))
        else:
            print("Wrong answer. The correct answer is :", random_question.answer)

        selected_category_copy.questions.remove(random_question)
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
        else:
            print("Choose either yes or no: ")


def game_starts():
    """docstring"""
    continue_playing = True

    total_score = 0
    json_file_path = "myquiz.json"
    category_list = get_category_list(json_file_path)

    user_input_name = startup()

    while continue_playing:

        selected_category = player_choose_category(category_list)

        selected_category_copy = copy.deepcopy(selected_category)

        # Select question, get answer and get point
        total_score += question_and_answer(selected_category_copy, total_score)

        print("Round is finished " + user_input_name + "! Score: " + str(total_score))

        # Keep playing or not
        continue_playing = player_wants_to_continue_playing()


def main():
    """docstring"""
    # Start game
    game_starts()


if __name__ == "__main__":
    main()
