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

# Start a new game, initializing snake and food
def start_game():
    global snake, food
    snake = Snake()
    food = Food()
    next_turn(snake, food)  # Start the game loop
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
BACKGROUND_COLOUR = "#000000"

# Main game loop
def next_turn(snake, food):
    x, y = snake.coordinates[0]  # Get the current position of the snake's head

    # Update the snake's direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Add the new head position to the snake's coordinates
    snake.coordinates.insert(0, (x, y))

    # Create a new rectangle for the updated head position
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
    snake.squares.insert(0, square)

    # Check if the snake eats the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1  # Increase the score
        label.config(text="Score:{}".format(score))  # Update score display
        canvas.delete("food")  # Remove the current food
        food = Food()  # Generate new food
    else:
        # Remove the last part of the snake's body to simulate movement
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collisions
    if check_collisions(snake):
        game_over()  # End the game if a collision occurs
    else:
        # Schedule the next frame
        window.after(SPEED, next_turn, snake, food)
