import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game - CodSoft - Task 4")
        self.root.geometry("600x400")
        self.root.configure(bg="#C64449")
        self.center_window(600, 400)
        
        self.player_score = 0
        self.ai_score = 0

        colors = {
            "bittersweet": "#C64449",
            "space-cadet": "#372E5F",
            "button-bg": "#372E5F"
        }
        
        self.color_bittersweet = colors["bittersweet"]
        self.color_spacecadet = colors["space-cadet"]
        self.button_color = colors["button-bg"]

        self.logo_frame = tk.Frame(self.root, bg=self.color_spacecadet)
        self.logo_frame.grid(row=0, column=0, columnspan=3, pady=10)

        image_path = "c:/Users/calls/Downloads/CodSoft/codsoft.png"
        if not os.path.isfile(image_path):
            print(f"Image file not found at path: {image_path}")
        else:
            self.logo_image = Image.open(image_path)
            self.logo_image = self.logo_image.resize((70, 70))
            self.logo = ImageTk.PhotoImage(self.logo_image)
            logo_label = tk.Label(master=self.logo_frame, image=self.logo, bg=self.color_spacecadet)
            logo_label.pack()

        self.create_ui()
    
    def create_ui(self):
        self.rock_btn = tk.Button(self.root, text="Rock", command=lambda: self.play_round("Rock"), font=("Arial", 12), bg=self.button_color, fg="white")
        self.rock_btn.grid(row=1, column=0, padx=20, pady=10)

        self.paper_btn = tk.Button(self.root, text="Paper", command=lambda: self.play_round("Paper"), font=("Arial", 12), bg=self.button_color, fg="white")
        self.paper_btn.grid(row=1, column=1, padx=20, pady=10)

        self.scissors_btn = tk.Button(self.root, text="Scissors", command=lambda: self.play_round("Scissors"), font=("Arial", 12), bg=self.button_color, fg="white")
        self.scissors_btn.grid(row=1, column=2, padx=20, pady=10)

        self.restart_btn = tk.Button(self.root, text="Play Again", command=self.reset_game, font=("Arial", 12), bg=self.button_color, fg="white")
        self.restart_btn.grid(row=2, column=1, padx=20, pady=20)

        self.player_choice_lbl = tk.Label(self.root, text="You: ", font=("Arial", 14), width=15, anchor='w', bg=self.color_bittersweet, fg="white")
        self.player_choice_lbl.grid(row=3, column=0, padx=20, pady=20)

        self.ai_choice_lbl = tk.Label(self.root, text="Computer: ", font=("Arial", 14), width=15, anchor='w', bg=self.color_bittersweet, fg="white")
        self.ai_choice_lbl.grid(row=3, column=2, padx=20, pady=20)

        self.result_lbl = tk.Label(self.root, text="", font=("Arial", 14), width=25, anchor='center', bg=self.color_bittersweet, fg="white")
        self.result_lbl.grid(row=4, column=0, columnspan=3, pady=10)

        self.player_score_lbl = tk.Label(self.root, text="User: 0", font=("Arial", 14), width=15, anchor='w', bg=self.color_bittersweet, fg="white")
        self.player_score_lbl.grid(row=5, column=0, padx=20, pady=10)

        self.ai_score_lbl = tk.Label(self.root, text="Computer: 0", font=("Arial", 14), width=15, anchor='w', bg=self.color_bittersweet, fg="white")
        self.ai_score_lbl.grid(row=5, column=2, padx=20, pady=10)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def determine_winner(self, player_choice, ai_choice):
        if player_choice == ai_choice:
            return "Draw"
        elif (player_choice == "Rock" and ai_choice == "Scissors") or \
             (player_choice == "Paper" and ai_choice == "Rock") or \
             (player_choice == "Scissors" and ai_choice == "Paper"):
            return "User"
        else:
            return "Computer"
    
    def play_round(self, player_choice):
        ai_choice = random.choice(["Rock", "Paper", "Scissors"])
        winner = self.determine_winner(player_choice, ai_choice)
        
        if winner == "User":
            self.player_score += 1
        elif winner == "Computer":
            self.ai_score += 1
        elif winner == "Draw":
            self.player_score += 1
            self.ai_score += 1
        
        self.update_ui(player_choice, ai_choice, winner)
    
    def update_ui(self, player_choice, ai_choice, winner):
        self.player_choice_lbl.config(text=f"You: {player_choice}")
        self.ai_choice_lbl.config(text=f"Computer: {ai_choice}")
        self.result_lbl.config(text=f"Result: {winner}")
        self.player_score_lbl.config(text=f"User: {self.player_score}")
        self.ai_score_lbl.config(text=f"Computer: {self.ai_score}")
    
    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.player_score_lbl.config(text="User: 0")
        self.ai_score_lbl.config(text="Computer: 0")
        self.result_lbl.config(text="")
        self.player_choice_lbl.config(text="You: ")
        self.ai_choice_lbl.config(text="Computer: ")

root = tk.Tk()
game = RPSGame(root)
root.mainloop()
