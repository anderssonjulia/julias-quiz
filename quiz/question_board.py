"""docstr"""

import random

class QuestionBoard:
    """docstr"""

    def __init__(self):
        self.question_list = []

    def __len__(self):
        return len(self.question_list)

    def randomize(self):
        """docstr"""
        random.shuffle(self.question_list)

    def pop_question(self):
        """docstr"""
        return self.question_list.pop()
    
    def append(self, question):
        return self.question_list.append(question)

    @staticmethod
    def filter_by_selected_difficulty(selected_difficulty, question_list):
        """docstr"""
        # Iterate through all the questions
        # Add them to a list if their difficulty matches the chosen one

        question_board = QuestionBoard()

        for question in question_list:
            if selected_difficulty == question.difficulty.lower():
                question_board.append(question)

# quiz/question_board.py:32:16: E1101: Instance of 'QuestionBoard' has no 'append' member (no-member)
# Fixa som Alex gjorde

        return question_board
