"User"

from jinja2 import Environment, FileSystemLoader


class User:
    # pylint: disable=too-few-public-methods
    """Has username and score attributes that are initially None and 0."""

    def __init__(self, username=None, score=0):
        self.username = username
        self._score = score

    def save_user_score(self, user):
        file_loader = FileSystemLoader("template")
        env = Environment(loader=file_loader)
        template = env.get_template("highscore.j2")

        # Render the template with the user's score
        output = template.render(username=user.username, user_score=user._score)

        # Write the rendered HTML to a file
        with open("docs/highscore.html", "w") as f:
            f.write(output)

        print("User score saved to highscore.j2")

    @property
    def score(self):
        "Score"
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
