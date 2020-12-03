from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("purple")
timmy.forward(100)

screen.canvheight = 120
screen.canvwidth = 120
screen.exitonclick()
