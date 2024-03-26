import json
from pathlib import Path

class QuizQuestion():
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

    questions_json_file_path = Path("questions.json")

    @staticmethod
    def create_quiz_question_list_from_json(questions_json_file_path):
        with open(questions_json_file_path, "r") as json_file:
            json_data = json_file.read()

        quiz_question_dict_list = json.loads(json_data)
        
        quiz_question_list = []

        for quiz_question_dict in quiz_question_dict_list:
            quiz_question = QuizQuestion(
                quiz_question_dict["question"], quiz_question_dict["answer"], quiz_question_dict["difficulty"]
            )
            quiz_question_list.append(quiz_question)

        return quiz_question_list

    @staticmethod
    def filter_by_difficulty(difficulty, quiz_question_list):
        filtered_question_list = []
        for quiz_question in quiz_question_list:
            if difficulty == quiz_question.difficulty:
                filtered_question_list.append(quiz_question)

        return filtered_question_list