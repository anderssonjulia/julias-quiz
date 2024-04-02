import enum
class Difficulty(enum.Enum):
    easy = enum.auto()
    medium = enum.auto()
    hard = enum.auto()
    
    @staticmethod
    def from_str(difficulty):
        if difficulty.lower() == "easy":
            return Difficulty.easy
        elif difficulty.lower() == "medium":
            return Difficulty.medium
        elif difficulty.lower() == "hard":
            return Difficulty.hard
        else:
            raise ValueError(f"Unknown difficulty {difficulty}")


class Question():
    def __init__(self, difficulty):
        self.difficulty = Difficulty.from_str(difficulty)

question = Question("medium")
selected_difficulty = Difficulty.from_str(input("Enter difficulty: "))


selected_difficulty == question.difficulty