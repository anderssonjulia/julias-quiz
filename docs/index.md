# Homepage?

## Leaderboard

<iframe src="highscore.html" width="100%" height="500px"></iframe>

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Code examples

### Codeblocks

jag tror att `detta` borde vara kod

### Plain codeblock

Detta borde vara ett kodblock:

```
Kodkodkod
def testar()
man kan kopiera den också!!!!
```

### Python codeblock

``` py
from testar import hej
def hejhej()
```

### With a title

``` py title="jag testar"
def hej()
    lista = [1, 2, 3]
    while len(lista) > 0:
        lista.pop()
        print("vad gör jag ens")
    return lista
```

### Line numbers

``` py linenums="1"
def hej()
    print("testar")
# detta borde vara linje 3
```

### Highlighted lines
``` py hl_lines="2 3"
def testar()
    print("highlighted")
    return highlighted
```

### Maxat codeblock
``` py title="kodblock" linenums="1" hl_lines="3 4 5 14 15"
def _start_round(input_manager, user, question_list):

    selected_difficulty = input_manager.get_selected_difficulty()
    question_board = QuestionBoard.filter_by_selected_difficulty(
        selected_difficulty, question_list
    )
    question_board.randomize()

    score = 0
    while len(question_board) > 0:
        question = question_board.pop_question()
        user_question_answer = input_manager.get_answer(question)

        if question.is_correct(user_question_answer):
            score += 1

        print()

    user.score += score
```