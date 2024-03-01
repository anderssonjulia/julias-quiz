import json
import random
import sys
import copy

#classes for the json-file
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
    
class Answer:
    def __init__(self, answer):
        self.answer = answer

#import json-file
json_file_path = '/home/jande182/work/myquiz/myquiz.json'

with open(json_file_path, "r") as json_file:
    json_data = json_file.read()

data = json.loads(json_data)
categories = [Category(**c) for c in data["categories"]]

#points
points = 0

#choosing difficulty
print("QUIZ")
print()
user_input_name = input("Username: ").lower()

a = 5

while a == 5:
    selected_category = None

    while not selected_category:
        user_input = input("Choose the difficulty of the quiz: (Easy/Medium/Hard) ").lower()
        print()
        
        for category in categories:
            if category.name.lower() == user_input:
                selected_category = category
                break

        if selected_category == None:
            print("Choose either easy, medium or hard!")
    
    selected_category2 = copy.deepcopy(selected_category)

    while selected_category2.questions:

        #game starts
        random_question = selected_category2.get_random_questions()

        user_input = input(f"{random_question.question} ")

        #result
        if user_input.lower() == random_question.answer.lower():
            points = points + 1
            print("Right answer!!! Score: " + str(points))
        else:
            print("Wrong answer. The correct answer is :", random_question.answer)

        selected_category2.questions.remove(random_question)
        print()

    print("Round is finished " + user_input_name + "! Score: " + str(points))


    #keep playing or not
    continue_playing = None

    while continue_playing != "yes" and continue_playing != "no":
        continue_playing = input("Do you want to keep playing? (Yes/No) ").lower()
        print()

        for continue_playing in input():
            if continue_playing == "yes" or continue_playing == "no":
                break

        if continue_playing != "yes" and continue_playing != "no":
            print("Choose either yes or no: ")