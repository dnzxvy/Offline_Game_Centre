from tkinter import *
from tkinter import messagebox
import random

# Define the Snake class to manage the snake's properties and movement
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS  # Initial size of the snake
        self.coordinates = []  # List to store the coordinates of each body part
        self.squares = []  # List to store the visual representation of the snake parts

        # Initialise snake body at the top-left corner of the canvas
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])  # Snake starts at [0, 0]

        # Create the graphical representation of the snake
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)

# Define the Food class to manage food placement and appearance
class Food:
    def __init__(self):
        # Randomly generate coordinates for the food within the game boundaries
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]  # Store the food's coordinates

        # Create the visual representation of the food
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")


# Define the Poison food class to manage its appearance and placement

class PoisonFood:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=POISON_FOOD_COLOUR, tag="poison_food")
        # Randomly generate coordinates for the poisoned food within the game boundaries

# Start a new game, initializing snake and food
def start_game():
    global snake, food, poison_food
    snake = Snake()
    food = Food()
    poison_food = PoisonFood()
    next_turn(snake, food, poison_food)  # Start the game loop
    start_button.destroy()  # Remove the start button after the game starts
    restart_button.place_forget()
    game_over_label.place_forget()

# Restart the game after a game over
def restart_game():
    global score
    score = 0  # Reset the score
    label.config(text="Score:{}".format(score))  # Update score display
    game_over_label.place_forget()  # Hide "Game Over" message
    restart_button.place_forget()  # Hide restart button
    start_game()  # Start a new game

# Constants for game settings
GAME_WIDTH =500
GAME_HEIGHT = 500
SPEED = 47
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
POISON_FOOD_COLOUR = "#A020F0"
BACKGROUND_COLOUR = "#000000"

# Main game loop
def next_turn(snake, food, poison_food):
    x, y = snake.coordinates[0]

    # Update the snake's direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Add the new head position
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
    snake.squares.insert(0, square)

    # Check if the snake eats the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    elif x == poison_food.coordinates[0] and y == poison_food.coordinates[1]:
        score -= 2
        label.config(text="Score:{}".format(score))
        canvas.delete("poison_food")
        poison_food = PoisonFood()

        # Delete all snake squares
        for square in snake.squares:
            canvas.delete(square)
        snake.squares.clear()
        snake.coordinates.clear()

        # End the game
        game_over()


    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collisions
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food, poison_food)

# Change the snake's direction based on user input
def change_direction(new_direction):
    global direction
    # Prevent the snake from reversing direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

# Check for collisions with walls or the snake's body
def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Check if the snake hits the wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    # Check if the snake collides with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Display the "Game Over" screen
def game_over():
    canvas.delete(ALL)  # Clear the canvas
    game_over_label.place(relx=0.5, rely=0.4, anchor=CENTER)  # Display "Game Over" message
    restart_button.place(relx=0.5, rely=0.6, anchor=CENTER)  # Show restart button

# Initialize the main Tkinter window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# Initialize game variables
score = 0
direction = 'down'

# Create and configure the score label
label = Label(window, text="Score:{}".format(score), font=('consolas', 46))
label.pack()

# Create and configure the game canvas
canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack(fill=BOTH, expand=True)

# Add the start button
start_button = Button(window, text="Start Game", font=('consolas', 20), command=start_game, bd=0)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
window.update()  # Update the window to render the start button

# Create "Game Over" label and restart button
game_over_label = Label(window, text="Game Over!", font=('consolas', 44), fg="red")
restart_button = Button(window, text="Restart Game", font=('consolas', 20), command=restart_game, bd=0)
restart_button.place_forget()  # Hide restart button initially

# Center the game window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind keyboard inputs to change the snake's direction
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Start the Tkinter event loop
window.mainloop()

