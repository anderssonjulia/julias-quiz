"User"


class User:
    # pylint: disable=too-few-public-methods
    """Has username and score attributes that are initially None and 0."""

    def __init__(self, username=None, score=0):
        self.username = username
        self._score = score

    @property
    def score(self):
        "Score"
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
