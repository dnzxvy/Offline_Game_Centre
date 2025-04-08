import tkinter as tk
import random
import time


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Arcade")

        self.start_frame = tk.Frame(root, bg="black")
        self.start_frame.pack(fill="both", expand=True)

        self.title_label = tk.Label(self.start_frame, text="TIC-TAC-TOE", font=("Courier", 40, "bold"), fg="yellow",
                                    bg="black")
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(self.start_frame, text="START GAME", font=("Courier", 24, "bold"), fg="black",
                                      bg="cyan", width=15, height=2, command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        self.start_frame.destroy()
        TicTacToeGUI(self.root)


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.board = [' ' for _ in range(9)]
        self.current_turn = 'X'

        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(master, text='', font=('normal', 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.current_turn
            color = 'blue' if self.current_turn == 'X' else 'red'
            bg_color = 'lightblue' if self.current_turn == 'X' else 'lightcoral'
            self.buttons[square].config(text=self.current_turn, fg=color, bg=bg_color)

            if self.check_winner(square):
                self.show_win_message()
                return
            elif ' ' not in self.board:
                self.show_tie()
                return

            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            if self.current_turn == 'O':
                self.master.after(500, self.computer_move)  # slight delay for realism

    def computer_move(self):
        available_moves = [i for i, spot in enumerate(self.board) if spot == ' ']
        if available_moves:
            square = random.choice(available_moves)
            self.make_move(square)

    def check_winner(self, square):
        row = square // 3
        if self.board[row * 3] == self.board[row * 3 + 1] == self.board[row * 3 + 2] != ' ':
            return True

        col = square % 3
        if self.board[col] == self.board[col + 3] == self.board[col + 6] != ' ':
            return True

        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True

        return False

    def show_win_message(self):
        popup = tk.Toplevel(self.master)
        popup.title("🎉 WINNER! 🎉")
        popup.geometry("300x200")
        popup.configure(bg="black")

        label = tk.Label(popup, text=f"{self.current_turn} WINS!", font=("Courier", 24, "bold"), fg="yellow",
                         bg="black")
        label.pack(expand=True)

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
            button.config(text='', fg='black', bg='SystemButtonFace')
        self.current_turn = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
