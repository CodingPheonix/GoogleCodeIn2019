var questionList = ["cat", "dog"];
var questionsCorrect = 0;
var round = 1;

function SubmitButton() {

    var x, text;
  
    x = document.getElementById("textEntry").value;

    if (x.length > 1){
        if (x.toLowerCase() == questionList[round-1]){
            document.getElementById("output").innerHTML = "You got it right!";
            questionsCorrect += 1;
        } else {
            document.getElementById("output").innerHTML = "You got it wrong, the correct answer is " + questionList[round-1] + "<br \>";

        }

        setTimeout(function(){ 
            nextRound();
        }, 1250);
    } else {
        document.getElementById("output").innerHTML = "Please enter a valid answer";
    }
}

function nextRound(){

    round += 1;
    document.getElementById("textEntry").value = "";

    if (round < 3) {

        document.getElementById("questionNum").innerHTML = "Question #"+round;
        document.getElementById("output").innerHTML = "Answer in the text box below and hit submit";
        document.getElementById("image").src = "images/"+questionList[round-1]+".png";
    
    } else {
        gameOver();
    }
}

function gameOver(){

    document.getElementById("input").style.visibility = "hidden";
    document.getElementById("retryButton").style.visibility = "visible";

    document.getElementById("questionNum").innerHTML = "Game Over<br />Score: "+questionsCorrect+"/"+questionList.length;
    if (questionsCorrect/questionList.length >= 0.5){
        document.getElementById("output").innerHTML = "You did it!<br />Congrats on passing this quiz";
        document.getElementById("image").src = "images/check.png";

    } else {
        document.getElementById("output").innerHTML = "Better luck next time! :(";
        document.getElementById("image").src = "images/cross.png";
    }
}

function resetQuiz(){
    round = 1;
    questionsCorrect=0;
    document.getElementById("retryButton").style.visibility = "hidden";
    document.getElementById("input").style.visibility = "visible";
    document.getElementById("questionNum").innerHTML = "Question #"+round;
    document.getElementById("output").innerHTML = "Answer in the text box below and hit submit";
    document.getElementById("image").src = "images/"+questionList[round-1]+".png";
}