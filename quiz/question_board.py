from quiz.question import Question


import random


class QuestionBoard:
    """docstr"""

    def __init__(self):
        self.selected_question = Question

    # self.selected_question_list = [QuizQuestion]
    # Om det första alternativet är rätt så är ju QuestionBoard typ en kopia
    # av QuizQuestion klassen fast med de valda frågorna endast, då kan man
    # kanske göra QuestionBoard till en child class av QuizQuestion
    # Om det är den andra så skapas ett object av QuestionBoard för varje runda,
    # Då är QuestionBoard-objekten en listor av QuizQuestions
    # På rad 233 används längden av QuestionBoard-objektet vilket man också
    # kanske borde tänka på, att ändra så att det funkar ihop med den sorten

    def add_question(self, question):
        """docstr"""
        self.selected_question.append(question)

    def get_questions(self):
        """docstr"""
        return self.selected_question

    def get_random_question(self):
        """docstr"""
        random.seed(21)
        return random.choice(self.selected_question)

    def remove_question(self):
        """docstr"""
        self.selected_question.remove

    @staticmethod
    def filter_by_selected_difficulty(selected_difficulty, quiz_question_list):
        """docstr"""
        # Iterate through all the questions
        # Add them to a list if their difficulty matches the chosen one

        selected_question_list = QuestionBoard()

        for quiz_question in quiz_question_list:
            if selected_difficulty == quiz_question.difficulty:
                # selected_quiz_question = QuestionBoard(
                #     quiz_question["question"],
                #     quiz_question["answer"]
                # )
                # filtered_question_list.append(selected_quiz_question)
                selected_question_list.append(quiz_question)

        return selected_question_list
