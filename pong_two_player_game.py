from tkinter import Tk, Canvas, messagebox
import random
import time
import winsound

# Draw a purple background on the canvas
def draw_star_background(canvas):
    canvas.create_rectangle(0, 0, 700, 500, fill="#1a0033", outline="")

    for _ in range(100):  # Randomly generate 100 tiny white stars
        x = random.randint(0, 700)
        y = random.randint(0, 500)
        size = random.randint(1, 2)
        canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")

# Ball class — manages the ball's movement, collisions, and score
class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.p1S = 0  # Score for Player 1 (left)
        self.p2S = 0  # Score for Player 2 (right)
        self.drawP1 = None
        self.drawP2 = None
        self.id = self.canvas.create_oval(10, 10, 35, 35, fill=color)
        self.canvas.move(self.id, 327, 220)  # Start position
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x = random.choice([-2.5, -2.5])  # Random horizontal start
        self.y = -2.5  # Vertical movement speed

    # Check if a player has won the game (score of 8)
    def check_winner(self):
        winner = None
        if self.p1S == 8:
            winner = "Player Left"
        if self.p2S == 8:
            winner = "Player Right"
        return winner

    # Update left player’s score display
    def updateP1(self, val):
        self.canvas.delete(self.drawP1)
        self.drawP1 = self.canvas.create_text(170, 50, font=('', 40), text=str(val), fill='white')

    # Update right player’s score display
    def updateP2(self, val):
        self.canvas.delete(self.drawP2)
        self.drawP2 = self.canvas.create_text(530, 50, font=('', 40), text=str(val), fill='red')

    # Collision detection for left paddle
    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    # Collision detection for right paddle
    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    # Update ball position and handle wall/paddle/score logic
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # Bounce off top and bottom
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4

        # Scored on left side (Player 2 scores)
        if pos[0] <= 0:
            self.p2S += 1
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.canvas.move(self.id, 327, 220)  # Reset position
            self.x = 4
            self.updateP2(self.p2S)

        # Scored on right side (Player 1 scores)
        if pos[2] >= self.canvas_width:
            self.p1S += 1
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.canvas.move(self.id, -327, -220)  # Reset position
            self.x = -4
            self.updateP1(self.p1S)

        # Bounce off paddles
        if self.hit_paddle1(pos):
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.x = -4
        if self.hit_paddle2(pos):
            winsound.PlaySound('Beep2.wav', winsound.SND_FILENAME)
            self.x = 4

# Left paddle class (Player 1)
class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 200, 20, 310, fill=color)
        self.y = 0
        self.canvas.bind_all('<KeyPress-w>', self.move_up)
        self.canvas.bind_all('<KeyPress-s>', self.move_down)

    # Move up on W key
    def move_up(self, e):
        self.y = -5

    # Move down on S key
    def move_down(self, e):
        self.y = 5

    # Update paddle position with bounds
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = 0

# Right paddle class (Player 2)
class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(680, 200, 710, 310, fill=color)
        self.y = 0
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)

    # Move up on Up Arrow key
    def move_up(self, e):
        self.y = -5

    # Move down on Down Arrow key
    def move_down(self, e):
        self.y = 5

    # Update paddle position with bounds
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 500:
            self.y = 0

# 🪟 Initialize the main game window
tk = Tk()
tk.title("Pong Game!!!")
tk.geometry("+300+100")  # Place it nicely on screen
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)  # Keeps window on top

# Create the game canvas
canvas = Canvas(tk, width=700, height=500, bd=0, highlightthickness=0)
canvas.pack()

draw_star_background(canvas)  # Draw starry background
canvas.create_line(350, 0, 350, 500, fill='white')  # Mid divider

tk.update()


paddle1 = Paddle1(canvas, 'purple')
paddle2 = Paddle2(canvas, 'purple')
ball = Ball(canvas, paddle2, paddle1, 'white')

#  Main game loop
while True:
    ball.draw()
    paddle1.draw()
    paddle2.draw()

    if ball.check_winner():
        messagebox.showinfo("Game Has Ended", ball.check_winner() + " Won!!")
        break

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)  # Controls game speed


tk.mainloop()
