from turtle import Turtle,Screen
import random

is_race_on=False

screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bet","Which turtle is going to win the race? Enter a color:").lower()

colors=["red","orange","yellow","green","blue","purple"]
all_turtles=[]

y=70

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.teleport(-230, y)
    all_turtles.append(new_turtle)
    y-=30


if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print("You've won!")
            else:
                print("You lose...")
            print(f"The winning turtle is {winning_color}")
            is_race_on=False

        rand_distance = random.randint(0,10)
        turtle.penup()
        turtle.forward(rand_distance)


screen.exitonclick()
