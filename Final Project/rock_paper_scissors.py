'''
04/06/2024
CSE 111-07
Nicholas Wilkins 
Final Project: Rock Paper Scissors With GUI
'''
import tkinter as tk
import random
 
# Initialize round counters
player_wins = 0
computer_wins = 0
 
def determine_winner(player_choice, computer_choice):
    '''
    Determine the winner of a rock-paper-scissors game between a player and the computer.

    Parameters:
    - player_choice (str): The choice made by the player. Valid options are "rock", "paper", or "scissors".
    - computer_choice (str): The choice made by the computer. Valid options are "rock", "paper", or "scissors".

    Returns:
    - tuple: A message indicating the result ("It's a tie!", "You win!", or "Computer wins!") and the computer's choice.

    Modifies:
    - player_wins (int): A global variable tracking the number of wins by the player.
    - computer_wins (int): A global variable tracking the number of wins by the computer.
    '''
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
 
def play_round(player_choice):
    '''
    Plays a single round of rock-paper-scissors against the computer.

    Parameters:
    - player_choice (str): The choice made by the player. Valid options are "rock", "paper", or "scissors".

    Returns:
    - tuple: The result of the round as a message ("It's a tie!", "You win!", or "Computer wins!") and the computer's choice.

    Calls:
    - determine_winner(player_choice, computer_choice): A function to determine the winner of the round.
    '''
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result, computer_choice = determine_winner(player_choice, computer_choice)
    return result, computer_choice
 
def update_status(result, computer_choice):
    '''
    Update the game status labels and check for a game winner.

    Parameters:
    - result (str): The result of the round ("It's a tie!", "You win!", or "Computer wins!").
    - computer_choice (str): The choice made by the computer ("rock", "paper", or "scissors").

    Modifies:
    - status_label (Label): The label widget that displays the result of the round.
    - score_label (Label): The label widget that displays the ongoing score.
    - computer_choice_label (Label): The label widget that displays the computer's choice.
    - rock_button, paper_button, scissors_button (Button): The button widgets for player's choices.

    Behavior:
    Updates the text of the status, score, and computer choice labels with the latest round results and scores.
    If either the player or the computer wins three times, disables the choice buttons and displays the overall winner.
    '''
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

def play_again():
    '''
    Reset the game to play another round of rock-paper-scissors.

    This function resets the game's status and counters, clears the player's choice, and re-enables the choice buttons.

    Modifies:
    - player_wins (int): A global variable tracking the number of wins by the player, reset to 0.
    - computer_wins (int): A global variable tracking the number of wins by the computer, reset to 0.
    - player_choice (StringVar): A tkinter StringVar object holding the player's choice, cleared.
    - status_label (Label): The label widget that displays the game status, cleared.
    - score_label (Label): The label widget that displays the ongoing score, reset.
    - computer_choice_label (Label): The label widget that displays the computer's choice, cleared.
    - rock_button, paper_button, scissors_button (Button): The button widgets for player's choices, set to active.
    '''
    global player_wins, computer_wins

    # Clear player's choice
    player_choice.set("") 

    # Clear game status 
    update_status("", "")
    
    # Reset round counters
    player_wins = 0 
    computer_wins = 0

    # Reset the score label, game status, and computer choice label
    status_label.config(text="")
    score_label.config(text=f"Player: {player_wins} | Computer: {computer_wins}")
    computer_choice_label.config(text="")

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
if __name__ == "__main__":
    root.mainloop()