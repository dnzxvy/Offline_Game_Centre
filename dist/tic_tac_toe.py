import tkinter as tk
import time


class TicTacToeApp:
    def __init__(self, root):
        self.root = root  # Stores Tkinter window
        self.root.title("Tic Tac Toe ")


        self.start_frame = tk.Frame(root, bg="black") # Creates frame widget for start screen elements
        self.start_frame.pack(fill="both", expand=True) # Fills window with black background

        self.title_label = tk.Label(self.start_frame, text="TIC-TAC-TOE", font=("Courier", 40, "bold"), fg="yellow",
                                    bg="black") # Creates Bold yellow title
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(self.start_frame, text="START GAME", font=("Courier", 24, "bold"), fg="black",
                                      bg="cyan", width=15, height=2, command=self.start_game) # Creates bright cyan start game button
        self.start_button.pack(pady=20)

    def start_game(self):
        self.start_frame.destroy()  # Remove start screen
        TicTacToeGUI(self.root)  # Launch game


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = [' ' for _ in range(9)] # Represents 3x3 grid
        self.current_turn = 'X' # Player turn starts with X

        self.buttons = []
        for i in range(9): # Loops through 9 position with each representing a square
            row, col = divmod(i, 3) # Converts into 2d grid coordinates
            button = tk.Button(master, text='', font=('Helvetica', 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i)) # Button created representing a square
            button.grid(row=row, column=col)
            self.buttons.append(button) # Each button is saved

    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.current_turn
            colour = 'Purple' if self.current_turn == 'X' else 'red'
            bg_color = 'lightblue' if self.current_turn == 'X' else 'lightcoral'
            self.buttons[square].config(text=self.current_turn, fg=colour, bg=bg_color)

            # Check for a winner
            if self.check_winner(square):
                return

            # Check for a tie after checking for a winner
            if ' ' not in self.board:
                self.show_tie()
                return

            # Switch turns
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self, square):
        row_ind = square // 3 # Calculate which row the move belongs to via division
        row = self.board[row_ind * 3: (row_ind + 1) * 3] # Extracts the row from the board list
        if all([spot == self.current_turn for spot in row]): # Checks if all spots in row match player symbol 'X' or 'O'
            self.show_win_message() # If true, the player wins
            return True

        col_ind = square % 3 # Determines the column based on remainder
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == self.current_turn for spot in column]): # Checks if the entire column belongs to current player
            self.show_win_message()
            return True

        if square % 2 == 0: # Check for diagonal winners
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Checks diagonal from top left to bottom right
            if all([spot == self.current_turn for spot in diagonal1]):
                self.show_win_message()
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # Checks diagonal from top right to bottom left
            if all([spot == self.current_turn for spot in diagonal2]):
                self.show_win_message()
                return True

        return False # If no win was found

    def show_win_message(self):
        popup = tk.Toplevel(self.master) # Creates popup window
        popup.title(" WINNER! ")
        popup.geometry("300x200") # Size of popup window
        popup.configure(bg="black")

        label = tk.Label(popup, text=f"{self.current_turn} WINS!", font=("Courier", 24, "bold"), fg="yellow",
                         bg="black")
        label.pack(expand=True) # Centres the label inside the popup

        # Flashing Effect
        for _ in range(5):
            popup.update()
            label.config(fg="red")
            time.sleep(0.2)
            popup.update()
            label.config(fg="yellow")
            time.sleep(0.2)

        popup.destroy()
        self.reset_game()

    def show_tie(self):
        popup = tk.Toplevel(self.master)
        popup.title("🤝 It's a Tie! 🤝")
        popup.geometry("300x200")
        popup.configure(bg="black")

        label = tk.Label(popup, text="It's a Tie!", font=("Courier", 24, "bold"), fg="cyan", bg="black")
        label.pack(expand=True)


        for _ in range(5):
            popup.update()
            label.config(fg="magenta")
            time.sleep(0.2)
            popup.update()
            label.config(fg="cyan")
            time.sleep(0.2)

        popup.destroy()
        self.reset_game()

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text='', fg='black', bg='SystemButtonFace')  # Reset text, color, and background
        self.current_turn = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
