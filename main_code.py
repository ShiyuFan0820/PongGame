from turtle import Screen
from Paddle import Paddle
from Ball import Ball
import time


# Create the screen.
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# Create the paddle class.
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def move_up(self):
        if self.ycor() < 325:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -320:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


# Create the ball class.
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def y_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1


# Create the score class.
class Score(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x_position, y_position)
        self.color("white")
        self.hideturtle()
        self.write(self.score, font=("Courier", 50, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, font=("Courier", 50, "normal"))

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"Game Over! The winner is {winner}!", align="center",
                   font=("Courier", 20, "normal"))


# Create the paddle and ball objects.
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
# Create the score objects.
r_score = Score(200, 330)
l_score = Score(-200, 330)
# Control the paddle with keys.
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    if r_score.score == 11:
        is_game_on = False
        r_score.game_over("Right Player")
    elif l_score.score == 11:
        is_game_on = False
        l_score.game_over("Left Player")
    else:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        # Detect collision with walls.
        if ball.ycor() > 370 or ball.ycor() < -360:
            ball.y_bounce()
        # Detect collision with paddles.
        if ball.distance(r_paddle) < 50 and ball.xcor() > 335:
            r_score.add_score()
            ball.x_bounce()
        elif ball.distance(l_paddle) < 50 and ball.xcor() < -345:
            l_score.add_score()
            ball.x_bounce()
        elif ball.xcor() > 500:
            l_score.add_score()
            ball.reset_ball()
        elif ball.xcor() < -500:
            r_score.add_score()
            ball.reset_ball()

screen.exitonclick()
