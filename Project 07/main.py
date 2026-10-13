
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x420")
root.resizable(False, False)

# Game variables
current_player = "X"
buttons = []

# Check winner
def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if (buttons[a]["text"] == buttons[b]["text"]
                == buttons[c]["text"] != ""):
            messagebox.showinfo(
                "Game Over",
                f"Player {buttons[a]['text']} wins!"
            )
            reset_game()
            return True

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return True

    return False


# Handle button clicks
def make_move(index):
    global current_player

    if buttons[index]["text"] == "":
        buttons[index].config(text=current_player)

        if not check_winner():
            current_player = "O" if current_player == "X" else "X"
            status_label.config(
                text=f"Player {current_player}'s turn"
            )


# Reset the game
def reset_game():
    global current_player

    current_player = "X"

    for button in buttons:
        button.config(text="")

    status_label.config(text="Player X's turn")


# Title
title_label = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=10)

# Current player status
status_label = tk.Label(
    root,
    text="Player X's turn",
    font=("Arial", 14)
)
status_label.pack(pady=5)

# Game board
board = tk.Frame(root)
board.pack(pady=10)

for i in range(9):
    button = tk.Button(
        board,
        text="",
        font=("Arial", 24, "bold"),
        width=4,
        height=2,
        command=lambda i=i: make_move(i)
    )
    button.grid(row=i // 3, column=i % 3, padx=3, pady=3)
    buttons.append(button)

# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)
restart_button.pack(pady=10)

# Start the application
root.mainloop()
