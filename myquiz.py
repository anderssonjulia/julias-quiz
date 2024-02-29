import json
import random
#import time
import sys

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
    
#def reset_timer():
#    return time.time()

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
user_input_name = input("Användarnamn: ").lower()

user_input = input("Vilken svårighetsgrad vill du ha på quizet? (Lätt/Medel/Svårt) ").lower()
print()

selected_category = next((c for c in categories if c.name.lower() == user_input), None)

while not selected_category:
    user_input2 = input("Välj antingen lätt, medel eller svår! ").lower()
    if user_input2 not in ['lätt'] and user_input2 not in ['medel'] and user_input2 not in ['svår']:
        sys.exit()
    else: 
        print()

#    time_limit = 10
    
while selected_category.questions:

        #game starts
        random_question = selected_category.get_random_questions()

        #start_time = reset_timer()

        user_input = input(f"{random_question.question} ")
        
        #elapsed_time = time.time() - start_time

        #if elapsed_time > time_limit:
        #    print("Tiden är slut!")
        #    break

        #result
        if user_input.lower() == random_question.answer.lower():
            points = points + 1
            print("Rätt svar!!! Poäng: " + str(points))
        else:
            print("Fel svar. Rätt svar är:", random_question.answer)

        selected_category.questions.remove(random_question)

        #keep playing or not
        print()
        continue_playing = input("Vill du fortsätta? (Ja/Nej) ").lower()
        if continue_playing not in ['ja'] and continue_playing not in ['nej']:
            continue_playing2 = input("Välj antingen ja eller nej: ").lower()
            if continue_playing2 not in ['ja'] and continue_playing2 not in ['nej']:
                break
            else:
                print()
                continue

        elif continue_playing == 'ja':
            print()
            continue
        elif continue_playing == 'nej':
            sys.exit()