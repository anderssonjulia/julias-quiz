"Quiz"

from quiz.question_board import QuestionBoard


def _print_quiz_header():
    """Print the header."""
    print("QUIZ")
    print()


def _start_round(input_manager, user, question_list):
    """Start round of the quiz with the selected difficulty. Runs until
    the question board is empty. If the iser input is correct, a point is added
    to User score. If it is not, the correct answer is printed."""

    selected_difficulty = input_manager.get_selected_difficulty()
    question_board = QuestionBoard.filter_by_selected_difficulty(
        selected_difficulty, question_list
    )
    question_board.randomize()

    score = 0
    while len(question_board) > 0:
        question = question_board.pop_question()
        user_question_answer = input_manager.get_answer(question)

        if question.is_correct(user_question_answer):
            score += 1

        print()

    user._score += score


def start_quiz(input_manager, question_list, user):
    """Call all of the functions and initialize the objects to run the quiz.
    Start round and after each one, print score and check if the player wants to continue.
    """
    # Start game
    _print_quiz_header()

    input_manager.get_username(user)

    continue_playing = True

    while continue_playing:
        _start_round(input_manager, user, question_list)
        print(f"Round is finished {user.username}! Total score: {user._score}")
        continue_playing = input_manager.does_player_want_to_continue_playing(user)
