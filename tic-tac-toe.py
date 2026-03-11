# TIC TAC TOE - [ GUI ]

import tkinter as tk

root = tk.Tk()
root.title("TIC TAC TOE")

buttons = []
board = [""] * 9
current_player = "X"


def disable_buttons():
    for button in buttons:
        button.config(state="disabled")


def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def reset_game():
    global current_player
    current_player = "X"

    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", state="normal", bg="SystemButtonFace")

    result_label.config(text="Current Player - X")


def click(position):
    global current_player

    if board[position] == "":
        board[position] = current_player

        if current_player == "X":
            buttons[position].config(text="X", bg="lightblue")
        else:
            buttons[position].config(text="O", bg="lightcoral")

        if check_winner(current_player):
            result_label.config(text=f"Winner = {current_player}")
            disable_buttons()
            return

        if current_player == "X":
            current_player = "O"
            result_label.config(text="Current Player - O")
        else:
            current_player = "X"
            result_label.config(text="Current Player - X")


for i in range(3):
    for j in range(3):
        button = tk.Button(
            root,
            text="",
            height=3,
            width=10,
            font=("Arial",20),
            command=lambda pos=i*3+j: click(pos)
        )
        button.grid(row=i, column=j)
        buttons.append(button)


result_label = tk.Label(root, text="Current Player - X", font=("Arial",12))
result_label.grid(row=3, column=0, columnspan=3)


reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
