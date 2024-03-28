class User:
    """docstr"""

    def __init__(self, score=0):
        self.score = score

    def set_username(self):
        """docstr"""
        username = input("Username: ")
        return username

    def add_score(self, score):
        """docstr"""
        score += 1
        return self.score

    def get_score(self):
        """docstr"""
        return self.score
