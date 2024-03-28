class InputManager():
    """The quiz manager is the head of the quiz. It communicates with the QuestionBoard and QuizUser classes."""
    def initialize_all_questions(question_file_path):
        with open(question_file_path, "r") as json_file:

        json_data = json_file.read(question_file_path)

    def initialize_user():
        pass

    def start_quiz():
        pass





    def get_random_question(self, selected_question_list):
        """docstr"""
        random.seed(21)
        return random.choice(selected_question_list)

    def check_answer(
        self, random_question, selected_questions_list, user_answer, score
    ):
        """docstr"""
        if random_question.is_correct(user_answer):
            score += 1
            print("Right answer!!! Score: " + str(score))
        else:
            print("Wrong answer. The correct answer is :", random_question.answer)

        selected_questions_list.remove(random_question)
        print()

        return selected_questions_list, score

    def get_answer_input(self, random_question):
        """docstr"""

        # AttributeError: 'list' object has no attribute 'get_random_questions'
        user_answer = input(f"{random_question.question}")

        return user_answer, random_question

# Ska alla klasser och funktioner vara på samma nivå, vilket de är nu, eller ska de vara under quiz_manager.py eftersom den interagerar med alla?
# 