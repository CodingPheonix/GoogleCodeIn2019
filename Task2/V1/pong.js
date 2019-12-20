//Instantiate and declare variables
const width = 1080;
const height = 720;
const paddleWidth = 10;
const paddleHeight = 100;
const ballSize = 10;
const k = 1.5;
const paddleOffset = 25;
var newFrame = false;
var first = true;
var ballSpeed = 10;
var y = height/2-paddleHeight/2;
var centerX, centerY, d;
var FPS = 30;
var score1 = 0;
var score2 = 0;
var enter = false;
var ball = {
    x:width/2,
    y:height/2,
    xvel:-1,
    yvel:Math.random()*2-1
};

var paddle2 = {
    y:height/2,
    direction:1,
}

//Get 2D context for canvas element
ctx = document.getElementById("Pong").getContext("2d");
ctx.canvas.width = width;
ctx.canvas.height = height;

ctx.textAlign = "center";

//Keyhandler for when they click
document.addEventListener('keydown', function(event) {
    if (event.keyCode == 13) {
        enter = true;
    }
}, true);

document.addEventListener('keyup', function(event) {
    if (event.keyCode == 13) {
        enter = false;
    }
}, true);
//Mouse position handler
function findScreenCoords(mouseEvent)
{
  var xpos;
  var ypos;
  if (mouseEvent)
  {
    //FireFox
    ypos = mouseEvent.screenY;
  }
  else
  {
    //IE
    ypos = window.event.screenY;
  }
  y = ypos-86;
}
//Canvas element
document.getElementById("Pong").onmousemove = findScreenCoords;


function game (){
    
    if (score1 >= 5 || score2 >= 5){

        //Clear the screen
        ctx.clearRect(0,0,width, height)

        //Backgrounds
        ctx.fillStyle = "#c0c0c0";
        ctx.fillRect(0,0,width,height);
        ctx.fillStyle = "#000000";
        ctx.fillRect(0, 7.5, 1080, 705);

        // Draw the scores
        ctx.fillStyle = "#FFFFFF"
        ctx.font = "45px Arial"
        ctx.fillText(score1, 245, 75, 100);
        ctx.fillText(score2, 835, 75, 100);

        //Fixed paddle positions
        ctx.fillRect (paddleOffset, height/2 - paddleHeight/2, paddleWidth, paddleHeight);
        ctx.fillRect (width-paddleOffset-paddleWidth, height/2-paddleHeight/2, paddleWidth, paddleHeight);


        //Draw the wall

        ctx.fillStyle = "#808080"
        ctx.fillRect(width/2-5,7.5,10,height-15);

        ctx.font = "50px Arial" 
        ctx.fillStyle = "#E94747"
        ctx.fillRect(width/2-175, 25, 350, 75)
        ctx.fillStyle = "#47BDE9"
        ctx.fillText((score1>=5?"Player":"Computer") + " wins", width/2, 75, 300)
        ctx.fillStyle = "#000000";
        ctx.fillRect(width/2-75, height/2-50, 150, 100);
        ctx.fillStyle = "#FFFFFF";
        ctx.fillText("Press Enter to restart", width/2, 360, 300);
        if (enter){
            console.log(score1, score2);
            score1 = 0;
            score2 = 0;
            ballSpeed = 10;
            ball = {
                x:width/2,
                y:height/2,
                xvel:-1,
                yvel:Math.random()*2-1
            };            
        }
    } else if (first){

        //Backgrounds
        ctx.fillStyle = "#c0c0c0";
        ctx.fillRect(0,0,width,height);
        ctx.fillStyle = "#000000";
        ctx.fillRect(0, 7.5, 1080, 705);

        // Draw the scores
        ctx.fillStyle = "#FFFFFF"
        ctx.font = "45px Arial"
        ctx.fillText(score1, 245, 75, 100);
        ctx.fillText(score2, 835, 75, 100);

        //Draw the wall

        ctx.fillStyle = "#808080"
        ctx.fillRect(width/2-5,7.5,10,height-15);

        //Instructions
        ctx.font = "50px Arial"
        ctx.fillStyle = "#000000";
        ctx.fillRect(width/2-75, height/2-50, 150, 100);
        ctx.fillStyle = "#FFFFFF"
        ctx.fillText("Press Enter to start", width/2, 360, 300);

        // First game fixed paddle positions

        ctx.fillStyle = "#47BDE9"
        ctx.fillRect (paddleOffset, height/2 - paddleHeight/2, paddleWidth, paddleHeight);
        ctx.fillStyle = "#E94747"
        ctx.fillRect (width-paddleOffset-paddleWidth, height/2-paddleHeight/2, paddleWidth, paddleHeight);

        if (enter){
            first = false;
        }
    
    } else {


        //Clear the screen
        ctx.clearRect(0,0,width, height)

        //Backgrounds
        ctx.fillStyle = "#c0c0c0";
        ctx.fillRect(0,0,width,height);
        ctx.fillStyle = "#000000";
        ctx.fillRect(0, 7.5, 1080, 705);

        // Draw the scores
        ctx.fillStyle = "#FFFFFF"
        ctx.font = "45px Arial"
        ctx.fillText(score1, 245, 75, 100);
        ctx.fillText(score2, 835, 75, 100);

        //Draw the wall

        ctx.fillStyle = "#808080"
        ctx.fillRect(width/2-5,7.5,10,height-15);


        //Computer ai

        if (ball.y > paddle2.y+paddleHeight/2){
            paddle2.direction = 1;
        } else {
            paddle2.direction = -1;
        }

        paddle2.y = paddle2.y + Math.sqrt(ball.yvel**2+ball.xvel**2) * paddle2.direction * ballSpeed * 0.55;
        //Drawing the paddles
        if (y <= 7.5+paddleHeight/2){
            y=7.5+paddleHeight/2;
        } else if (y >= height-7.5-paddleHeight/2){
            y=height-7.5-paddleHeight/2;
        }

        if (paddle2.y <= 7.5){
            paddle2.y=7.5;
        } else if (paddle2.y >= height-7.5-paddleHeight){
            paddle2.y=height-7.5-paddleHeight;
        }

        ctx.fillStyle = "#47BDE9"
        ctx.fillRect(paddleOffset, y-paddleHeight/2, paddleWidth, paddleHeight);
        ctx.fillStyle = "#E94747"
        ctx.fillRect(width-paddleOffset-paddleWidth, paddle2.y, paddleWidth, paddleHeight);

        //Update ball position and speed

        ball.x = ball.x + ball.xvel*ballSpeed;
        ball.y = ball.y + ball.yvel*ballSpeed;

        //Wall bounce mechanics

        if (ball.y <= ballSize || ball.y >= height-ballSize){
            ball.yvel = -ball.yvel;
            ballSpeed = 1.05 * ballSpeed;
        }

        //Paddle bounce mechanics

        if  (paddleOffset < ball.x + ballSize &&
            paddleOffset + paddleWidth > ball.x &&
            y-paddleHeight/2 < ball.y + ballSize &&
            y-paddleHeight/2 + paddleHeight > ball.y) {
            
            d = Math.abs(y-ball.y);
            
            ballSpeed = 1.05 * ballSpeed;
            ball.x = paddleOffset+paddleWidth+ballSize+1;
            ball.xvel = -ball.xvel;
            ball.yvel = (ball.yvel / Math.abs(ball.yvel)) * (d / (paddleHeight/2)) * k * Math.abs(ball.xvel);
        }

        if  (width-paddleWidth-paddleOffset < ball.x + ballSize &&
            width-paddleWidth-paddleOffset + paddleWidth > ball.x &&
            paddle2.y < ball.y + ballSize &&
            paddle2.y + paddleHeight > ball.y) {
            
            d = Math.abs(paddle2.y-ball.y);
            
            ball.x = width-paddleOffset-paddleWidth-ballSize-1;
            ball.xvel = -ball.xvel;
            ball.yvel = (ball.yvel / Math.abs(ball.yvel)) * (d / (paddleHeight/2)) * k * Math.abs(ball.xvel);

        }
        


        //Draw the ball

        centerX = ball.x-(ballSize/2);
        centerY = ball.y-(ballSize/2);

        ctx.fillStyle = "#E5EC15";

        ctx.beginPath();
        ctx.arc(centerX, centerY, ballSize, 0, 2 * Math.PI, false);
        ctx.fill();


        //Update scores and reset ball if necessary

        if (ball.x >= width){
            score1++;
            ball = {
                x:width/2,
                y:height/2,
                xvel:-1,
                yvel:Math.random()*2-1
            };
            ballSpeed = 10;
        } else if (ball.x <= 0){
            score2++;
            ball = {
                x:width/2,
                y:height/2,
                xvel:-1,
                yvel:Math.random()*2-1
            };
            ballSpeed = 10;
        };       
    }
}
setInterval (game, FPS);