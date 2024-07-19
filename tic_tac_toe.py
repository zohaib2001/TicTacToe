import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        """
        Initialize the game with the given root window.
        """
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.game_mode = None

    def create_widgets(self):
        """
        Create the initial widgets for the game.
        """
        tk.Label(self.root, text="Tic-Tac-Toe", font=("Helvetica", 20), fg="blue").grid(row=0, column=0, columnspan=3)
        tk.Button(self.root, text="Play with a Friend", command=lambda: self.start_game("friend"), font=("Helvetica", 12), bg="green", fg="black").grid(row=1, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Play with the Computer", command=lambda: self.start_game("computer"), font=("Helvetica", 12), bg="orange", fg="black").grid(row=2, column=0, columnspan=3, pady=10)

    def start_game(self, mode):
        """
        Start the game with the selected mode (against a friend or computer).
        """
        self.game_mode = mode
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=5, height=2, command=lambda row=i, col=j: self.player_move(row, col), bg="light gray")
                self.buttons[i][j].grid(row=i+3, column=j)

    def player_move(self, row, col):
        """
        Handle the player's move.
        """
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col].config(state="disabled", disabledforeground="black" if self.current_player == "X" else "red")
            self.board[row][col] = self.current_player
            self.root.update()
            if self.check_winner(self.current_player):
                self.root.after(500, lambda: self.end_game(f"Player {self.current_player} wins!"))
            elif self.check_draw():
                self.root.after(500, lambda: self.end_game("The game is a draw!"))
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.game_mode == "computer" and self.current_player == "O":
                    self.root.after(500, self.computer_move)

    def computer_move(self):
        """
        Handle the computer's move.
        """
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if self.buttons[row][col]["text"] == " ":
                self.buttons[row][col]["text"] = "O"
                self.buttons[row][col].config(state="disabled", disabledforeground="red")
                self.board[row][col] = "O"
                break
        self.root.update()
        if self.check_winner("O"):
            self.root.after(500, lambda: self.end_game("Computer wins!"))
        elif self.check_draw():
            self.root.after(500, lambda: self.end_game("The game is a draw!"))
        else:
            self.current_player = "X"

    def check_winner(self, player):
        """
        Check if the given player has won.
        """
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]]
        ]
        return [player, player, player] in win_conditions

    def check_draw(self):
        """
        Check if the game is a draw.
        """
        return all(cell != " " for row in self.board for cell in row)

    def end_game(self, message):
        """
        End the game and show the result.
        """
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        """
        Reset the game for a new round.
        """
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "
                self.buttons[i][j].config(state="normal", bg="light gray")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
