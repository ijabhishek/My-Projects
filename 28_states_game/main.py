# Import the necessary libraries
import pandas
import turtle

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("India States Game")

# Load the background image
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data from CSV
data = pandas.read_csv("state_list.csv")
all_states = data.state.to_list()
guessed_states = []

# Game loop: continue until 28 states are correctly guessed
while len(guessed_states) < 28:
    # Prompt user for a state name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name? ").title()
    
    # Check if the guessed state is valid and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        # Add the state to the list of guessed states
        guessed_states.append(answer_state)
        
        # Create a turtle for displaying the state name
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        # Get coordinates for the state
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        
        # Display the state name
        t.write(answer_state)
