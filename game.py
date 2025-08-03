import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "exit":
            print("\nThanks for playing! Final Score:")
            print(f"Your score: {user_score}")
            print(f"Computer score: {computer_score}")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Current Score ➤ You: {user_score} | Computer: {computer_score}")
        print("-" * 40)

# Run the game
play_game()
