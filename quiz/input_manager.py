"""docstr"""


class InputManager:
    """The quiz manager is the head of the quiz. It communicates with the QuestionBoard and QuizUser
    classes."""

    @staticmethod
    def get_selected_difficulty():
        """docstr"""

        selected_difficulty = None

        while selected_difficulty is None:
            player_choose_difficulty = input(
                "Choose the difficulty of the quiz: (Easy/Medium/Hard) "
            ).lower()
            print()

            if player_choose_difficulty in ("easy", "medium", "hard"):
                selected_difficulty = player_choose_difficulty

            # Run this as long as no valid difficulty is passed in
            if selected_difficulty is None:
                print("Choose either easy, medium or hard!")

        return selected_difficulty

    @staticmethod
    def does_player_want_to_continue_playing():
        """docstr"""

        while True:
            yes_or_no = input("Do you want to keep playing? (Yes/No) ").lower()
            print()

            if yes_or_no == "yes":
                return True
            if yes_or_no == "no":
                return False
            print("Choose either yes or no: ")

    @staticmethod
    def get_answer(question):
        """docstr"""
        return input(f"{question.question}")

    @staticmethod
    def get_username(user):
        """docstr"""
        return input(f"{user.username}")
