import random
import tkinter as tk
from tkinter import messagebox

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    bot_choice = random.choice(options)

    if choice == bot_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and bot_choice == "Scissors") or \
         (choice == "Paper" and bot_choice == "Rock") or \
         (choice == "Scissors" and bot_choice == "Paper"):
        result = "You Win! 🎉"
    else:
        result = "You Lose 😢"

    messagebox.showinfo(
        "Result",
        f"You chose: {choice}\nBot chose: {bot_choice}\n\n{result}"
    )

#  Window Setup 
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# Title
tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Helvetica", 18, "bold"),
    bg="#f4f4f4",
    fg="#333"
).pack(pady=15)

# Instruction 
tk.Label(
    root,
    text="Choose your move",
    font=("Helvetica", 12),
    bg="#f4f4f4",
    fg="#555"
).pack(pady=5)

# Button Frame
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=20)

# Buttons 
tk.Button(
    btn_frame,
    text="🪨 Rock",
    width=15,
    font=("Helvetica", 11),
    bg="#ff7675",
    fg="black",
    activebackground="#d63031",
    command=lambda: play("Rock")
).pack(pady=5)

tk.Button(
    btn_frame,
    text="📄 Paper",
    width=15,
    font=("Helvetica", 11),
    bg="#74b9ff",
    fg="black",
    activebackground="#0984e3",
    command=lambda: play("Paper")
).pack(pady=5)

tk.Button(
    btn_frame,
    text="✂️ Scissors",
    width=15,
    font=("Helvetica", 11),
    bg="#55efc4",
    fg="#2d3436",
    activebackground="#00b894",
    command=lambda: play("Scissors")
).pack(pady=5)

root.mainloop()
