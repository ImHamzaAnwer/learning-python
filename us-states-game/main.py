import turtle
import pandas as pd

screen = turtle.Screen()
image = "us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

states_data = pd.read_csv("us-states-game/50_states.csv")
state_names = states_data.state.to_list()
guessed_states = []


game_is_on = len(guessed_states) != len(state_names)
while game_is_on:
    user_guess = screen.textinput(
        f"Guess state {len(guessed_states)}/{len(state_names)}",
        "Guess the name of this state ?",
    ).title()

    if user_guess == "Exit":
        not_guessed = []
        for state in state_names:
            if state not in guessed_states:
                not_guessed.append(state)

        new_data = pd.DataFrame(not_guessed)
        new_data.to_csv("us-states-game/missed_states.csv")

        break

    if user_guess in state_names and user_guess not in guessed_states:
        state_row = states_data[states_data["state"] == user_guess]
        t = turtle.Turtle("circle")
        t.shapesize(0.3, 0.3)
        t.penup()
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(user_guess)
        guessed_states.append(user_guess)

        screen.update()


screen.mainloop()
