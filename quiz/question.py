"Question"

import json


class Question:
    """Each object has a question, answer and difficulty attribute."""

    def __init__(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def is_correct(self, user_answer):
        """Compare the user input to the answer of the Question object."""
        return user_answer.lower() == self.answer.lower()

    @staticmethod
    def create_quiz_question_list_from_json(questions_json_file_path):
        """Read the json-file and store it in a python list of dictionaries.
        For each dict object in the list, a Question object is being created.
        This object is added to the quiz_question_list."""
        # Read the json-file
        with open(questions_json_file_path, "r", encoding="utf-8") as json_file:
            json_data = json_file.read()

        # Store it in a python list of dicts
        question_dict_list = json.loads(json_data)

        question_list = []

        # Create a quiz_question object for each dict in the list
        # Add each quiz_question to the quiz_question_list
        for question_dict in question_dict_list:
            question = Question(
                question_dict["question"],
                question_dict["answer"],
                question_dict["difficulty"],
            )
            question_list.append(question)

        return question_list
