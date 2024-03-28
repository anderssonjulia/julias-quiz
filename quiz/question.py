# Get questions from the json-file
import json
from pathlib import Path


class Question:
    """docstr"""

    def __init__(self, question, answer, difficulty):
        """docstr"""
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def display_question(self):
        """docstr"""
        print(f"Question: {self.question}")

    def display_answer(self):
        """docstr"""
        print(f"Answer: {self.answer}")

    def is_correct(self, user_answer):
        """docstr"""
        return user_answer.lower() == self.answer.lower()

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
            quiz_question = Question(
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
            player_choose_difficulty = input(
                "Choose the difficulty of the quiz: (Easy/Medium/Hard) "
            ).lower()
            print()

            # Check if if any of the questions difficulty matches the user input
            # If they are equal, create a variable 'selected_difficulty' and pass the difficulty value
            for quiz_question in quiz_question_list:
                if quiz_question.difficulty.lower() == player_choose_difficulty:
                    selected_difficulty = quiz_question.difficulty

            # Run this as long as no valid difficulty is passed in
            if selected_difficulty is None:
                print("Choose either easy, medium or hard!")

        return selected_difficulty
