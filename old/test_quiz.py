from unittest.mock import patch

from main import main


# This testing file includes four different tests
# The first three of them includes different "keep playing" inputs (yes, no, maybe -> no)
# The fourth one has an invalid category input
# All of them test both correct and incorrect answer input


# Keep playing is no
def test_main_easy_no(capsys):
    input_dict = {}
    input_dict["username"] = "Julia"
    input_dict["difficulty"] = "Easy"
    input_dict["answer q1"] = "48"
    input_dict["answer q2"] = "1939"
    input_dict["answer q3"] = "mars"
    input_dict["answer q4"] = ""
    input_dict["answer q5"] = "william shakespeare"
    input_dict["answer q6"] = "avocado"
    input_dict["answer q7"] = "dont know"
    input_dict["answer q8"] = "Tokyo"
    input_dict["answer q9"] = "Rice"
    input_dict["answer q10"] = "i dont know"
    input_dict["keep playing"] = "No"

    my_input = [
        input_dict["username"],
        input_dict["difficulty"],
        input_dict["answer q1"],
        input_dict["answer q2"],
        input_dict["answer q3"],
        input_dict["answer q4"],
        input_dict["answer q5"],
        input_dict["answer q6"],
        input_dict["answer q7"],
        input_dict["answer q8"],
        input_dict["answer q9"],
        input_dict["answer q10"],
        input_dict["keep playing"],
    ]

    def get_input(text=""):
        return my_input.pop(0)

    expected = """QUIZ


Wrong answer. The correct answer is : Leonardo da Vinci

Wrong answer. The correct answer is : Elephant

Wrong answer. The correct answer is : Thomas Edison

Round is finished Julia! Total score: 7

"""

    with patch("builtins.input", side_effect=get_input):
        main()
    assert expected == capsys.readouterr().out


# Keep playing is yes
def test_main_easy_yes(capsys):
    input_dict = {}
    input_dict["username"] = "Julia"
    input_dict["difficulty"] = "Easy"
    input_dict["answer q1"] = "48"
    input_dict["answer q2"] = "1939"
    input_dict["answer q3"] = "mars"
    input_dict["answer q4"] = ""
    input_dict["answer q5"] = "william shakespeare"
    input_dict["answer q6"] = "avocado"
    input_dict["answer q7"] = "dont know"
    input_dict["answer q8"] = "Tokyo"
    input_dict["answer q9"] = "Rice"
    input_dict["answer q10"] = "i dont know"
    input_dict["keep playing"] = "Yes"
    input_dict["keep playing2"] = "No"

    my_input = [
        input_dict["username"],
        input_dict["difficulty"],
        input_dict["answer q1"],
        input_dict["answer q2"],
        input_dict["answer q3"],
        input_dict["answer q4"],
        input_dict["answer q5"],
        input_dict["answer q6"],
        input_dict["answer q7"],
        input_dict["answer q8"],
        input_dict["answer q9"],
        input_dict["answer q10"],
        input_dict["keep playing"],
        input_dict["difficulty"],
        input_dict["answer q1"],
        input_dict["answer q2"],
        input_dict["answer q3"],
        input_dict["answer q4"],
        input_dict["answer q5"],
        input_dict["answer q6"],
        input_dict["answer q7"],
        input_dict["answer q8"],
        input_dict["answer q9"],
        input_dict["answer q10"],
        input_dict["keep playing2"],
    ]

    def get_input(text=""):
        return my_input.pop(0)

    expected = """QUIZ

Wrong answer. The correct answer is : Leonardo da Vinci

Wrong answer. The correct answer is : Elephant

Wrong answer. The correct answer is : Thomas Edison

Round is finished Julia! Total score: 7

Wrong answer. The correct answer is : Leonardo da Vinci

Wrong answer. The correct answer is : Elephant

Wrong answer. The correct answer is : Thomas Edison

Round is finished Julia! Total score: 14

"""

    with patch("builtins.input", side_effect=get_input):
        main()
    assert expected == capsys.readouterr().out


# Keep playing is neither yes or no
def test_main_easy_neither(capsys):
    input_dict = {}
    input_dict["username"] = "Julia"
    input_dict["difficulty"] = "Easy"
    input_dict["answer q1"] = "48"
    input_dict["answer q2"] = "1939"
    input_dict["answer q3"] = "mars"
    input_dict["answer q4"] = ""
    input_dict["answer q5"] = "william shakespeare"
    input_dict["answer q6"] = "avocado"
    input_dict["answer q7"] = "dont know"
    input_dict["answer q8"] = "Tokyo"
    input_dict["answer q9"] = "Rice"
    input_dict["answer q10"] = "i dont know"
    input_dict["keep playing"] = "Maybe"
    input_dict["keep playing2"] = "Yes"
    input_dict["keep playing3"] = "No"

    my_input = [
        input_dict["username"],
        input_dict["difficulty"],
        input_dict["answer q1"],
        input_dict["answer q2"],
        input_dict["answer q3"],
        input_dict["answer q4"],
        input_dict["answer q5"],
        input_dict["answer q6"],
        input_dict["answer q7"],
        input_dict["answer q8"],
        input_dict["answer q9"],
        input_dict["answer q10"],
        input_dict["keep playing"],
        input_dict["keep playing2"],
        input_dict["difficulty"],
        input_dict["answer q1"],
        input_dict["answer q2"],
        input_dict["answer q3"],
        input_dict["answer q4"],
        input_dict["answer q5"],
        input_dict["answer q6"],
        input_dict["answer q7"],
        input_dict["answer q8"],
        input_dict["answer q9"],
        input_dict["answer q10"],
        input_dict["keep playing3"],
    ]

    def get_input(text=""):
        return my_input.pop(0)

    expected = """QUIZ


Wrong answer. The correct answer is : Leonardo da Vinci

Wrong answer. The correct answer is : Elephant

Wrong answer. The correct answer is : Thomas Edison

Round is finished Julia! Total score: 7

Choose either yes or no: 


Wrong answer. The correct answer is : Leonardo da Vinci

Wrong answer. The correct answer is : Elephant

Wrong answer. The correct answer is : Thomas Edison

Round is finished Julia! Total score: 14

"""

    with patch("builtins.input", side_effect=get_input):
        main()
    assert expected == capsys.readouterr().out


# Invalid difficulty
def test_main_invalid_difficulty(capsys):
    input_dict = {}
    input_dict["username"] = "Julia"
    input_dict["difficulty"] = "Esy"
    input_dict["difficulty2"] = "Easy"
    input_dict["answer q1"] = "48"
    input_dict["answer q2"] = "1939"
    input_dict["answer q3"] = "mars"
    input_dict["answer q4"] = ""
    input_dict["answer q5"] = "william shakespeare"
    input_dict["answer q6"] = "avocado"
    input_dict["answer q7"] = "dont know"
    input_dict["answer q8"] = "Tokyo"
    input_dict["answer q9"] = "Rice"
    input_dict["answer q10"] = "i dont know"
    input_dict["keep playing"] = "No"

    my_input = [
        input_dict["username"],
        input_dict["difficulty"],
        input_dict["difficulty2"],
        input_dict["answer q1"],
        input_dict["answer q2"],
        input_dict["answer q3"],
        input_dict["answer q4"],
        input_dict["answer q5"],
        input_dict["answer q6"],
        input_dict["answer q7"],
        input_dict["answer q8"],
        input_dict["answer q9"],
        input_dict["answer q10"],
        input_dict["keep playing"],
    ]

    def get_input(text=""):
        return my_input.pop(0)

    expected = """QUIZ


Choose either easy, medium or hard!

Wrong answer. The correct answer is : Leonardo da Vinci

Wrong answer. The correct answer is : Elephant

Wrong answer. The correct answer is : Thomas Edison

Round is finished Julia! Total score: 7

"""

    with patch("builtins.input", side_effect=get_input):
        main()
    assert expected == capsys.readouterr().out


def ask_question(selected_category_copy):
    """docstr"""
    random_question = selected_category_copy.get_random_questions()

    user_question_answer = input(f"{random_question.question} ")

    return user_question_answer, random_question


# @pytest.fixture
# def Mock_Category():
#     with patch("myquiz.Category") as mock_category:
#         yield mock_category

# def test_main_mock_questions(capsys, Mock_Category):
#     input_dict = {}
#     input_dict["username"] = "Julia"
#     input_dict["difficulty"] = "Easy"
#     input_dict["answer q1"] = "48"
#     input_dict["answer q2"] = "1939"
#     input_dict["answer q3"] = "mars"
#     input_dict["answer q4"] = ""
#     input_dict["answer q5"] = "william shakespeare"
#     input_dict["answer q6"] = "avocado"
#     input_dict["answer q7"] = "dont know"
#     input_dict["answer q8"] = "Tokyo"
#     input_dict["answer q9"] = "Rice"
#     input_dict["answer q10"] = "i dont know"
#     input_dict["keep playing"] = "No"

#     my_input = [

# input_dict["username"], input_dict["difficulty"], input_dict["answer q1"],
# input_dict["answer q2"], input_dict["answer q3"], input_dict["answer q4"],
# input_dict["answer q5"], input_dict["answer q6"], input_dict["answer q7"],
# input_dict["answer q8"], input_dict["answer q9"], input_dict["answer q10"],
# input_dict["keep playing"]

# ]
#     Category_instance = Mock_Category.return_value
#     Category_instance.name = "Easy"
#     Category_instance.questions = [Question("What is the capital of Japan?", "Tokyo") for i in range(0, 10)]
#     Category_instance.get_random_question.return_value = Question("What is the capital of Japan?", "Tokyo")
#     def get_input(text=""):
#         return my_input.pop(0)

#     expected =(
# f"""QUIZ


# Right answer!!! Score: 1

# Right answer!!! Score: 2

# Right answer!!! Score: 3

# Wrong answer. The correct answer is : Leonardo da Vinci

# Right answer!!! Score: 4

# Right answer!!! Score: 5

# Wrong answer. The correct answer is : Elephant

# Right answer!!! Score: 6

# Right answer!!! Score: 7

# Wrong answer. The correct answer is : Thomas Edison

# Round is finished Julia! Score: 7

# """)

#     with patch("builtins.input", side_effect=get_input):
#        main()
#     assert expected == capsys.readouterr().out


# def test_get_user_input_choose_difficulty():
#     test_cases = [("easy", "easy"), ("medium", "medium"), ("hard", "hard")]

#     for input_value, expected_result in test_cases:
#         with patch("builtins.input", return_value=input_value):
#             result = get_user_input_choose_difficulty()
#             assert result == expected_result


# def test_get_user_input_name():
#     with patch("builtints.input", return_value="Julia"):
#         result = get_user_imput_name()

#     assert result == "Julia"


# def test_get_CONTINUE_PLAYING():
#     test_cases = [("yes", "yes"), ("no", "no")]

#     for input_value, expected_result in test_cases:
#         with patch("builtins.input", return_value=input_value):
#             result = get_CONTINUE_PLAYING()
#             assert result == expected_result


# Reformat the code into a fixture

# # Inside game_starts() function
# user_question_answer = ask_question(random_question)

#             # Check if answer is correct
#             if random_question.is_correct(user_question_answer):

#                 score = score + 1
#                 print("Right answer!!! Score: " + str(score))
#             else:
#                 print("Wrong answer. The correct answer is :", random_question.answer)

#             selected_category_copy.questions.remove(random_question)
#             print()

#         print("Round is finished " + user_input_name + "! Score: " + str(score))

#         # Keep playing or not
#         continue_playing = player_wants_to_continue_playing()
