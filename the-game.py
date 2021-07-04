#THIS IS NEPIZPONG 

#DICTIONARY  -> Turtle

import turtle 

wn = turtle.Screen()
wn.title("NEPIZPONG by @du.baldini")
wn.bgcolor("light green")
wn.setup(width=1000, height=800)
wn.tracer(0)

#SCORE
score_a = 0 
score_b = 0

#PADDLE A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("navy")
paddle_a.penup()
paddle_a.goto(-450, 0)
paddle_a.shapesize(stretch_wid=8, stretch_len=1)

#PADDLE B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("navy")
paddle_b.penup()
paddle_b.goto(450, 0)
paddle_b.shapesize(stretch_wid=8, stretch_len=1)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#PEN - SCORING SYSTEM
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle
pen.goto(0, 360)
pen.write("P1: 0    P2: 0", align="center", font=("Candara", 28, "bold"))

#FUNCTION
def paddle_a_up():
  y = paddle_a.ycor()
  y += 40
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 40
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 40
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 40
  paddle_b.sety(y)

#KEYBOARD BINDING -> ACEITAR INPUTS DO TECLADO
wn.listen()
wn.onkeypress(paddle_a_up, "w")  #APERTAR w PARA MOVER A PADDLE PARA CIMA
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#MAIN GAME LOOP 

while True: 
  wn.update()

  #MOVING THE BALL
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  #CHECKING THE BORDERS
  if ball.ycor() > 390:
    ball.sety(390)
    ball.dy *= -1

  if ball.ycor() < -390:
    ball.sety(-390)
    ball.dy *= -1
  
  if ball.xcor() > 490:
    ball.goto(0, 0)
    ball.dx *= -1
    score_a += 1
    pen.clear()
    pen.write("P1: {}    P2: {}".format(score_a, score_b), align="center", font=("Candara", 28, "bold"))


  if ball.xcor() < -490:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write("P1: {}    P2: {}".format(score_a, score_b), align="center", font=("Candara", 28, "bold"))


  #PADDLE AND BALL COLLISIONS
  if (ball.xcor > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
    ball.setx(340)
    ball.dx *= -1

  if (ball.xcor > -440 and ball.xcor() < -450) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
    ball.setx(-340)
    ball.dx *= -1
