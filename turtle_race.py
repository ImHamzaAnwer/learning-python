import random
import turtle

colors = ["blue", "orange", "green", "purple"]

screen = turtle.Screen()
screen.setup(500, 400)
user_guess = screen.textinput("Bet", f"Whos gonna win the bet ? {str(colors)}")

racers = []
race_is_on = False

for num in range(len(colors)):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[num])
    offset = num * 50
    new_turtle.goto(-230, (-80 + offset))
    racers.append(new_turtle)

if user_guess:
    race_is_on = True

while race_is_on:
    for racer in racers:
        if racer.xcor() > 220:
            race_is_on = False
            winning_color = racer.pencolor()
            if winning_color == user_guess:
                print(f"You won ! {winning_color} won the race")
            else:
                print(f"You lost ! {winning_color} won the race")

        racer.forward(random.randint(1, 10))


screen.exitonclick()
