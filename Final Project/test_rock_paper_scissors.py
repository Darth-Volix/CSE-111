'''
04/06/2024
CSE 111-07
Nicholas Wilkins 
Final Project: Rock Paper Scissors With GUI (Test Program)
'''

import pytest 
from rock_paper_scissors import determine_winner

def test_determine_winner():
    # Initialize global variables for testing
    global player_wins, computer_wins
    player_wins = 0
    computer_wins = 0

    # Test cases
    test_cases = [
        # Tie scenario
        (("rock", "rock"), ("It's a tie!", "rock")),
        (("paper", "paper"), ("It's a tie!", "paper")),
        (("scissors", "scissors"), ("It's a tie!", "scissors")),
        # Player wins scenarios
        (("rock", "scissors"), ("You win!", "scissors")),
        (("paper", "rock"), ("You win!", "rock")),
        (("scissors", "paper"), ("You win!", "paper")),
        # Computer wins scenarios
        (("rock", "paper"), ("Computer wins!", "paper")),
        (("paper", "scissors"), ("Computer wins!", "scissors")),
        (("scissors", "rock"), ("Computer wins!", "rock")),
    ]

    for i, (input_choices, expected_output) in enumerate(test_cases):
        player_choice, computer_choice = input_choices
        result, computer_choice_actual = determine_winner(player_choice, computer_choice)
        assert result == expected_output[0], f"Test case {i+1} failed: Expected '{expected_output[0]}', but got '{result}'"
        assert computer_choice_actual == expected_output[1], f"Test case {i+1} failed: Expected computer choice '{expected_output[1]}', but got '{computer_choice_actual}'"

# Call the test function
pytest.main(["-v", "--tb=line", "-rN", __file__])
