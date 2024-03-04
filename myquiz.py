"""Module documentation for myquiz."""

import json
import random
import copy


# classes for the json-file
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

    def is_correct(self):
        """Check if the user's input is the correct answer."""
        return user_input.lower() == self.answer.lower()


class Category:
    """Class documentation for Category."""

    def __init__(self, name, questions):
        """Constructor documentation."""
        self.name = name
        self.questions = [Question(**q) for q in questions]

    def get_random_questions(self):
        """Functiondocumentation"""
        return random.choice(self.questions)

    def get_all_questions(self):
        """Get all questions in category."""
        return self.questions


# import json-file
JSON_FILE_PATH = "/home/jande182/work/myquiz/myquiz.json"

with open(JSON_FILE_PATH, "r", encoding="utf-8") as json_file:
    json_data = json_file.read()

data = json.loads(json_data)
categories = [Category(**c) for c in data["categories"]]

# points
POINTS = 0

# choosing difficulty
print("QUIZ")
print()
user_name = input("Username: ").lower()


SELECTED_CATEGORY = None

while not SELECTED_CATEGORY:
    user_input = input("Choose the difficulty of the quiz: (Easy/Medium/Hard) ").lower()
    print()

    for category in categories:
        if category.name.lower() == user_input:
            SELECTED_CATEGORY = category
            break

    if SELECTED_CATEGORY is None:
        print("Choose either easy, medium or hard!")

selected_category2 = copy.deepcopy(SELECTED_CATEGORY)

while selected_category2.questions:

    # game starts
    random_question = selected_category2.get_random_questions()

    user_input = input(f"{random_question.question} ")

    # result
    if user_input.lower() == random_question.answer.lower():
        POINTS = POINTS + 1
        print("Right answer!!! Score: " + str(POINTS))
    else:
        print("Wrong answer. The correct answer is :", random_question.answer)

    selected_category2.questions.remove(random_question)
    print()

print("Round is finished " + user_name + "! Score: " + str(POINTS))


# keep playing or not
CONTINUE_PLAYING = None

while CONTINUE_PLAYING not in ("yes", "no"):
    CONTINUE_PLAYING = input("Do you want to keep playing? (Yes/No) ").lower()
    print()

    for CONTINUE_PLAYING in input():
        if CONTINUE_PLAYING in ("yes", "no"):
            break

    if CONTINUE_PLAYING not in ("yes", "no"):
        print("Choose either yes or no: ")
