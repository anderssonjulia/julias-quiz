class User:
    """docstr"""

    def __init__(self, username=None, score=0):
        self.username = username
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
