import tkinter
from tkinter import messagebox
import random


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = [' ' for _ in range(9)]
        self.current_turn = 'X'

        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tkinter.Button(master, text='', font=('normal', 20), width=5, height=2,
                                    command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.current_turn
            self.buttons[square].config(text=self.current_turn)
            if self.check_winner(square):
                messagebox.showinfo("Game Over", f"{self.current_turn} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self, square):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == self.current_turn for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == self.current_turn for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == self.current_turn for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == self.current_turn for spot in diagonal2]):
                return True

        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text='')
        self.current_turn = 'X'




if __name__ == "__main__":
    root = tkinter.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
