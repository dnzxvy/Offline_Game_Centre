from tkinter import *
from tkinter import messagebox
import random
import pygame

class Snake:


    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])#by doing [0, 0] at the start of every game, the snake will
            #appear on the top left hand corner


        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE #ihad to put int because it can produce a float value if
        #game_width is not a multiple of space_size which did happen so by converting it to
        #an integer it works.
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")
        #x,y is the starting corner and the ending corner which would be x and y plus the
        #space_size. this piece of code is for the food


