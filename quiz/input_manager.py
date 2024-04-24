"Input manager"


class InputManager:
    """Include methods that handle user input such as get difficulty, continue playing, get answer
    and get username."""

    @staticmethod
    def get_selected_difficulty():
        """Demand user input and if it matches any difficulty, set "selected_difficulty" to that
        difficulty. If not, tell the user to choose easy, medium or hard. Loop continues until
        "selected_difficulty" is set."""

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
        """Demand user input. If it is equal to yes, return True,
        if it is equal to no, return False."""

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
        """Display the question and demand an user input."""
        return input(f"{question.question} ")

    @staticmethod
    def get_username(user):
        """Demand user to insert username."""
        return input(f"Username: {user.username}")
