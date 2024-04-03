"""docstr"""

import json

class Question:
    """docstr"""

    def __init__(self, question, answer, difficulty):
        """docstr"""
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def is_correct(self, user_answer):
        """docstr"""
        return user_answer.lower() == self.answer.lower()

    @staticmethod
    def create_quiz_question_list_from_json(questions_json_file_path):
        """docstr"""
        # Read the json-file
        with open(questions_json_file_path, "r", encoding="utf-8") as json_file:
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
