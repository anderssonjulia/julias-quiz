"User"

class User:
    """Has username and score attributes that are initially None and 0."""

    def __init__(self, username=None, score=0):
        self.username = username
        self._score = score

    "Score"
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
