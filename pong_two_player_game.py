from tkinter import Tk, Canvas, messagebox
import random
import os
import time
import winsound

#Ball class

class Ball:
    def __init__(self,canvas,paddle1,paddle2,color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.p1S = 0
        self.p2S = 0
        self.drawP1 = None
        self.drawP2 = None
        self.id = self.canvas.create_oval(10,10,35,35,fill = color)

        self.canvas.move(self.id,327,220)
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.x = random.choice([-2.5,-2.5])
        self.y = -2.5

        #Check for score crossing 8 which is the score you need to win
        def check_winner(self):
            winner = None
            if self.p1S == 8:
                winner = "Player Left"
            if self.p2S == 8:
                winner = "Player Right"

            return winner















































































































































#initialising the window

tk = Tk()
tk.title("Pong Game!!!")
tk.geometry("+300+100")
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1) #keeps widnow on top of desktop always


#creating the canvas

canvas = Canvas(tk,width=700,height=500,bd=0,highlightthickness=0)
canvas.config(bg='black')
canvas.pack()

tk.update()

#creating the middle line to reprsent which half belongs to its player
canvas.create_line(350,0,350,500,fill='white')
