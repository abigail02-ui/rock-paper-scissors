#to play stone papr scissor with computer 
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # <-- Add this import
import os

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
            (player == 'paper' and computer == 'rock') or \
            (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!" 


# --- High Scores Functionality ---
HIGHSCORE_FILE = "rps_highscores.txt"

def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    with open(HIGHSCORE_FILE, "r") as f:
        lines = f.readlines()
    scores = []
    for line in lines:
        try:
            name, score = line.strip().split(",")
            scores.append((name, int(score)))
        except:
            continue
    return scores

def save_highscore(name, score):
    scores = load_highscores()
    scores.append((name, score))
    # Keep only top 5 scores
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    with open(HIGHSCORE_FILE, "w") as f:
        for n, s in scores:
            f.write(f"{n},{s}\n")

def get_highscore_text():
    scores = load_highscores()
    if not scores:
        return "No high scores yet."
    text = "High Scores:\n"
    for idx, (name, score) in enumerate(scores, 1):
        text += f"{idx}. {name}: {score}\n"
    return text


# --- Tkinter GUI Implementation ---
class RPSGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0  # Track ties

        self.label = tk.Label(master, text="Choose your move:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, command=lambda: self.play('rock'))
        self.rock_button.grid(row=0, column=0, padx=5)
        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, command=lambda: self.play('paper'))
        self.paper_button.grid(row=0, column=1, padx=5)
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, command=lambda: self.play('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.scoreboard_label = tk.Label(master, text=self.get_scoreboard_text(), font=("Arial", 12), fg="blue")
        self.scoreboard_label.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=5)

        self.highscore_button = tk.Button(master, text="Show High Scores", command=self.show_highscores)
        self.highscore_button.pack(pady=5)

    def get_scoreboard_text(self):
        return (
            f"Scoreboard:\n"
            f"Player Wins: {self.player_score}\n"
            f"Computer Wins: {self.computer_score}\n"
            f"Ties: {self.tie_score}"
        )

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        elif result == "It's a tie!":
            self.tie_score += 1

        self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}")
        self.scoreboard_label.config(text=self.get_scoreboard_text())

    def quit_game(self):
        # Ask for player name if they have a nonzero score
        if self.player_score > 0:
            name = tk.simpledialog.askstring("High Score", "Enter your name for the high score list:")
            if name:
                save_highscore(name, self.player_score)
        messagebox.showinfo(
            "Game Over",
            f"Final Score:\nYou: {self.player_score}\nComputer: {self.computer_score}\nTies: {self.tie_score}"
        )
        self.master.destroy()

    def show_highscores(self):
        hs_text = get_highscore_text()
        messagebox.showinfo("High Scores", hs_text)


def main():
    root = tk.Tk()
    game = RPSGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()




