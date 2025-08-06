import turtle
import pandas as pd
import time

states_df = pd.read_csv("50_states.csv")
all_states = states_df["state"].to_list()
guessed_states = []
score = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=510, width=740)
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)
screen.tracer(0)  # Turn off automatic screen updates


def write_state_on_map(state_name, color="black"):
    state_row = states_df[states_df.state == state_name]
    marker = turtle.Turtle()
    marker.hideturtle()
    marker.penup()
    marker.color(color)
    marker.goto(state_row.x.item(), state_row.y.item())
    marker.write(f"{state_name}", align="center", font=("Arial", 8, "bold"))


while True:
    user_guess = screen.textinput(
        title=f"{score}/50 states guessed", prompt="Enter a state name: "
    )
    if user_guess is None:
        continue
    user_guess = user_guess.title()

    if user_guess == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]

        # Save missed states to a CSV
        pd.DataFrame(missed_states, columns=["state"]).to_csv(
            "states_to_learn.csv", index=False
        )
        print("Missed states saved to 'states_to_learn.csv'")

        # Show missed states in red on the map
        for missed_state in missed_states:
            write_state_on_map(missed_state, color="red")
            screen.update()  # Update the screen after each state
            time.sleep(0.2)  # Short delay for animation
        break

    if user_guess in all_states and user_guess not in guessed_states:
        write_state_on_map(user_guess)
        guessed_states.append(user_guess)
        score += 1
        screen.update()

    if len(guessed_states) == 50:
        break

screen.exitonclick()
