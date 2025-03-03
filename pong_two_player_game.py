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

    # Update the left paddle score
    def updateP1(self, val):
        self.canvas.delete(self.drawP1)
        self.drawP1 = self.canvas.create_text(170, 50,
        font=('', 40), text=str(val), fill='white')


    #Update the right paddle score
    def updateP2(self, val):
        self.canvas.delete(self.drawP2)
        self.drawP2 = self.canvas.create_text(530, 50,
        font=('', 40), text=str(val), fill='red')

    #Check for collisions of ball & paddle for paddle left (P1)

    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

            return False


    #Check for collisions of ball & paddle for the right paddle (P2)

    def hit_paddle2(self,pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

            return False

    #Drawing the ball plus check for all collisions

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4
        if pos[0] <= 0:
            self.p2S += 1  # Update paddle 2 score
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.canvas.move(self.id, 327, 220)
            self.x = 4
            self.updateP2(self.p2S)
        if pos[2] >= self.canvas_width:
            self.p1S += 1  # Update paddle 1 score
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.canvas.move(self.id, -327, -220)
            self.x = -4
            self.updateP1(self.p1S)
        if self.hit_paddle1(pos):
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.x = -4
        if self.hit_paddle2(pos):
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.x = 4



# Left paddle class (p1)
class Paddle1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0,200,20,310,fill=color)
        self.y = 0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-w>',self.left)
        self.canvas.bind_all('<KeyPress-s>',self.right) #binding to keys

    #moving the paddle
    def left(self,e):
        self.y = -5

    def right(self,e):
        self.y = 5
    #drawing the left paddle
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = -0


#right paddle (p2)
class Paddle2:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(680,200,710,310,fill=color)
        self.y = 0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>',self.left)
        self.canvas.bind_all('<KeyPress-Down>',self.right)

    def left(self,e):
        self.y = -5

    def right(self,e):
        self.y = 5

    #drawing the right paddle
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = 0

#Initialising the window

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

#The obJects

paddle1 = Paddle1(canvas,'purple')
paddle2 = Paddle2(canvas,'purple')
ball = Ball(canvas,paddle2,paddle1,'white')

while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    if ball.check_winner():
        messagebox.showinfo("Game Has Ended",ball.check_winner()+"Won!!")

        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
