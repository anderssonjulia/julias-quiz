import random


class QuestionBoard:
    """A new object of this class is created everytime a new quiz round is started.
    It contains the ten questions of the selected category."""

    def __init__(self):
        self.question_list = []

    def __len__(self):
        return len(self.question_list)

    def randomize(self):
        """Randomizes the order of the list in the QuestionBoard object."""
        random.shuffle(self.question_list)

    def pop_question(self):
        """Return a question and then remove it from the list."""
        return self.question_list.pop()

    def append(self, question):
        """Enable .append for QuestionBoard objects. Add to question_list."""
        return self.question_list.append(question)

    @staticmethod
    def filter_by_selected_difficulty(selected_difficulty, question_list):
        """Create a question_board object and iterate through all 30 questions.
        Sort out the ones with the selected difficulty and add them to question_board
        object in the question_list."""
        # Iterate through all the questions
        # Add them to a list if their difficulty matches the chosen one

        question_board = QuestionBoard()

        for question in question_list:
            if selected_difficulty == question.difficulty.lower():
                question_board.append(question)

        # quiz/question_board.py:32:16: E1101:
        # Instance of 'QuestionBoard' has no 'append' member (no-member)
        # Fixa som Alex gjorde

        return question_board
