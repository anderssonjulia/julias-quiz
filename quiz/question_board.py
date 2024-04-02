import random


class QuestionBoard:
    """docstr"""

    def __init__(self):
        self.question_list = []

    def __len__(self):
        return len(self.question_list)

    def randomize(self):
        random.shuffle(self.question_list)

    def pop_question(self):
        return self.question_list.pop()
    
    @staticmethod
    def filter_by_selected_difficulty(selected_difficulty, question_list):
        """docstr"""
        # Iterate through all the questions
        # Add them to a list if their difficulty matches the chosen one

        question_board = QuestionBoard()

        for question in question_list:
            if selected_difficulty == question.difficulty.lower():
                question_board.append(question)

        return question_board
