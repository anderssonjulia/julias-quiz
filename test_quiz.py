from unittest.mock import patch
from myquiz import main

def test_main(capsys):
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
    
    my_input = [
        
input_dict["username"], input_dict["difficulty"], input_dict["answer q1"], 
input_dict["answer q2"], input_dict["answer q3"], input_dict["answer q4"], 
input_dict["answer q5"], input_dict["answer q6"], input_dict["answer q7"], 
input_dict["answer q8"], input_dict["answer q9"], input_dict["answer q10"], 
input_dict["keep playing"]

]
    
    def get_input(text=""):
        return my_input.pop(0)

    expected =(
f"""
QUIZ

Username: Julia
Choose the difficulty of the quiz: (Easy/Medium/Hard) Easy

What is 8 * 6? 48
Right answer!!! Score: 1

In which year did World War II begin? 1939
Right answer!!! Score: 2

Which is the red planet? mars
Right answer!!! Score: 3

Who painted the Mona Lisa? 
Wrong answer. The correct answer is : Leonardo da Vinci

Who wrote Romeo and Juliet? william shakespeare
Right answer!!! Score: 4

What is the main ingredient in guacamole? avocado
Right answer!!! Score: 5

What is the largest mammal? dont know
Wrong answer. The correct answer is : Elephant

What is the capital of Japan? Tokyo
Right answer!!! Score: 6

What is the main ingredient in sushi? Rice
Right answer!!! Score: 7

Who invented electricity? i dont know
Wrong answer. The correct answer is : Thomas Edison

Round is finished j! Score: 7
Do you want to keep playing? (Yes/No) Yes


Choose the difficulty of the quiz: (Easy/Medium/Hard) 
""")
    input_value = ("Hej")
    print("hej")
    with patch("builtins.input", side_effect=get_input):
       main()
    assert expected == capsys.readouterr().out

def hej():
    pass




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
