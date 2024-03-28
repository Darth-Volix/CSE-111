import tkinter as tk
import random
 
# Initialize round counters
player_wins = 0
computer_wins = 0
 
# Function to determine the winner of a round
def determine_winner(player_choice, computer_choice):
    global player_wins, computer_wins
   
    if player_choice == computer_choice:
        return "It's a tie!", computer_choice
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        player_wins += 1
        return "You win!", computer_choice
    else:
        computer_wins += 1
        return "Computer wins!", computer_choice
 
# Function to play a round
def play_round(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result, computer_choice = determine_winner(player_choice, computer_choice)
    return result, computer_choice
 
# Function to update the game status
def update_status(result, computer_choice):
    status_label.config(text=result)
    score_label.config(text=f"Player: {player_wins} | Computer: {computer_wins}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    # Check if someone has won three times
    if player_wins == 3 or computer_wins == 3:
        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissors_button.config(state=tk.DISABLED)
        # Display overall winner
        if player_wins == 3:
            status_label.config(text="Congratulations! You win the game!")
        else:
            status_label.config(text="Computer wins the game!")

 
# Function to handle button click
def play_again():
    global player_wins, computer_wins
    player_choice.set("")  # Clear player's choice
    update_status("", "")  # Clear game status
    player_wins = 0  # Reset round counters
    computer_wins = 0

    # Set the buttons back to active
    rock_button.config(state=tk.ACTIVE)
    paper_button.config(state=tk.ACTIVE)
    scissors_button.config(state=tk.ACTIVE)
 
# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
 
# Create a variable to store player's choice
player_choice = tk.StringVar()
 
# Create GUI elements
label = tk.Label(root, text="Choose rock, paper, or scissors:")
rock_button = tk.Button(root, text="Rock", command=lambda: update_status(*play_round("rock")))
paper_button = tk.Button(root, text="Paper", command=lambda: update_status(*play_round("paper")))
scissors_button = tk.Button(root, text="Scissors", command=lambda: update_status(*play_round("scissors")))
status_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
score_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
computer_choice_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
play_again_button = tk.Button(root, text="Play Again", command=play_again)
 
# Arrange GUI elements
label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()
status_label.pack()
score_label.pack()
computer_choice_label.pack()
play_again_button.pack()
 
# Start the GUI event loop
root.mainloop()