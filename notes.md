
kvar att skriva: 
input_manager(4): test_get_selected_difficulty():,test_does_player_want_to_continue_playing():,test_get_answer():,test_get_username():
question_board(1): test_filter_by_selected_difficulty():
tot: 5


###########################

ska quiz.py ha ett eget system test eller räcker system test, eftersom det nästan är main?

test_create_quiz_question_list_from_json(): finns i test_quiz.py och testar både create och filter

###########################


Quizet börjar med att man utser en quiz manager. 
Quiz manager får alla frågor från json filen.
Quiz manager registrerar en ny användare.
    Väljer ett användarnamn.
    En user skapas.
        Score sätts till 0.

Quiz manager startar quizet.
    Quiz manager frågar användaren vilken svårighetsgrad den vill spela i.
    Quiz manager sorterar ut alla frågor i den valda kategorin.
    Quiz manager startar en quiz runda med det valda QuizBoardet.
        Quiz manager ställer frågorna och input ges av användaren.
            Quiz manager ställer första frågan och ber om input från användaren.
            Detta upprepas tills alla frågor ställs
    Efter alla frågor har ställs skickas användarens svarsformulär till Quiz manager som kontrollerar hur många poäng användaren fick. 
    Denna data sparas till en fil.
    Quiz manager frågar användaren om den vill fortsätta spela.
        Om ja: Quiz manager startar en ny runda av quizet.
        Om nej: Presentera resultat från quiz rundorna
