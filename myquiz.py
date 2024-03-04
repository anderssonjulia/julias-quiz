import json
import random
import copy


# classes for the json-file
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = [Question(**q) for q in questions]

    def get_random_questions(self):
        return random.choice(self.questions)


# import json-file
JSON_FILE_PATH = "/home/jande182/work/myquiz/myquiz.json"

with open(JSON_FILE_PATH, "r") as json_file:
    json_data = json_file.read()

data = json.loads(json_data)
categories = [Category(**c) for c in data["categories"]]

# points
POINTS = 0

# choosing difficulty
print("QUIZ")
print()
user_name = input("Username: ").lower()


selected_category = None

while not selected_category:
    user_input = input("Choose the difficulty of the quiz: (Easy/Medium/Hard) ").lower()
    print()

    for category in categories:
        if category.name.lower() == user_input:
            selected_category = category
            break

    if selected_category is None:
        print("Choose either easy, medium or hard!")

selected_category2 = copy.deepcopy(selected_category)

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
