import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    """Prompts the player for their choice and validates the input."""
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    while player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()
    return player_choice

def determine_winner(player, computer):
    """
    Determines the winner of a single round and returns the result.
    Returns: 'player', 'computer', or 'tie'
    """
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'player'
    else:
        return 'computer'

def play_game():
    """Main function to run the Rock, Paper, Scissors game."""
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        print("\n--- Current Score ---")
        print(f"Player: {player_score} | Computer: {computer_score}")
        
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        
        if result == 'player':
            print("You win this round!")
            player_score += 1
        elif result == 'computer':
            print("The computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
            
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\n--- Final Score ---")
            print(f"Player: {player_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()