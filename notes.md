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