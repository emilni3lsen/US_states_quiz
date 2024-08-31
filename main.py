import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()

state_data = pandas.read_csv("50_states.csv")
states_list = state_data.state.to_list()

game_is_on = True
while game_is_on:

    answer = screen.textinput(f"{50 - len(states_list)}/{50} States guessed", "Guess a state:").title()

    if answer in states_list:
        state = state_data[state_data.state == answer]
        x = state.x.item()
        y = state.y.item()
        pen.setpos(x, y)
        pen.write(answer, False, "center", ("Arial", 8, "normal"))
        states_list.remove(answer)
    
    if len(states_list) == 0:
        pen.setpos(0,260)
        pen.write("Good Job! You got them all :)", False, "center", ("Arial", 13, "normal"))
        game_is_on = False
        
    if answer == "Exit":
        pen.color("red")
        for unguessed_state in states_list:
            state = state_data[state_data.state == unguessed_state]
            x = state.x.item()
            y = state.y.item()
            pen.setpos(x, y)
            pen.write(unguessed_state, False, "center", ("Arial", 8, "normal"))
        pen.setpos(0,260)
        pen.write(f"You guessed {50-len(states_list)}/50. Good job!", False, "center", ("Arial", 13, "normal"))
        states_to_learn = pandas.DataFrame(states_list, index=[i + 1 for i in range(len(states_list))], columns=["Unguessed States"])
        states_to_learn.to_csv("states_to_learn.csv")
        game_is_on = False
        
            
screen.exitonclick()
