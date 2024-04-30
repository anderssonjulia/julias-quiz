import unittest

from quiz.user import User


def test_constructor():
    username = ""
    score = 0
    user = User(username, score)
    assert user.username == username
    assert user.score == score


def test_score():
    input_list = User()
    expected = 2
    input_list.score = expected
    assert input_list.score == expected

