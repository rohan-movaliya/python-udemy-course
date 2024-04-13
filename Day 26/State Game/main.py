import turtle
import pandas as pd

data = pd.read_csv("State Game/50_states.csv")
all_states = data.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "State Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# This is the method to know cordinates of image when we click print in console
# def get_mouse_click_corr(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()


guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()
    if answer_state == "Exit":
        # use list comprehension insted of for loop
        missing_state = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        df = pd.DataFrame(missing_state)
        df.to_csv("State Game/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(state_data.state.item())

screen.exitonclick()
