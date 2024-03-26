from quiz_question import QuizQuestion
from pathlib import Path

def test_constructor():
    question = "what is my test?"
    answer = "test_asnwer"
    difficulty = "easy"
    quiz_question = QuizQuestion(question, answer, difficulty)
    assert quiz_question.question == question
    assert quiz_question.answer == answer
    assert quiz_question.difficulty == difficulty 

def test_create_quiz_question_list_from_json():
    expected_easy_quiz_question_list_length = 10
    
    questions_json_file_path = Path("questions.json")
    quiz_question_list = QuizQuestion.create_quiz_question_list_from_json(questions_json_file_path)
    easy_quiz_question_list = QuizQuestion.filter_by_difficulty("Easy", quiz_question_list)
   
    assert len(easy_quiz_question_list) == expected_easy_quiz_question_list_length