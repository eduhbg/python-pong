import turtle

# Game state
start_game = False

# Window
width_value = 800
height_value = 600
window = turtle.Screen()
window.title("My First Game in Python")
window.bgcolor("black")
window.setup(width = width_value, height = height_value)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align =
"center", font = ("Corier", 24, "normal"))

# Level
level = turtle.textinput("Level Selector",
"Enter a level you want to play (1, 2, 3, 4 or 5): ")
max_score = int(turtle.textinput("Maximum Score",
"Enter the maximum number of points to win the match: "))

if level == "1":
    ball_speed = 0.25
    paddle_width = 5
    start_game = True
elif level == "2":
    ball_speed = 0.35
    paddle_width = 4
    start_game = True
elif level == "3":
    ball_speed = 0.45
    paddle_width = 3
    start_game = True
elif level == "4":
    ball_speed = 0.55
    paddle_width = 2
    start_game = True
elif level == "5":
    ball_speed = 0.75
    paddle_width = 1
    start_game = True
else:
    exit()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = paddle_width, stretch_len = 0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = paddle_width, stretch_len = 0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed

# Paddles movements functions and border checking
def paddle_a_up():
    if paddle_a.ycor() < height_value / 2:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > (height_value / 2) * -1:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() < height_value / 2:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > (height_value / 2) * -1:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Keyboard
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main Loop
while start_game:
    window.update()

    # Check the max score
    if score_a == max_score:
        pen.clear()
        pen.write("PLAYER 'A' WON THE GAME!", align = "center",
        font = ("Corier", 24, "normal"))
        ball_speed = 0
        ball.goto(0, 0)

    if score_b == max_score:
        pen.clear()
        pen.write("PLAYER 'B' WON THE GAME!", align = "center",
        font = ("Corier", 24, "normal"))
        ball_speed = 0
        ball.goto(0, 0)

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b),
        align = "center", font = ("Corier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b),
        align = "center", font = ("Corier", 24, "normal"))

    # Collision of the ball with paddles
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() <
    paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() <
    paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1