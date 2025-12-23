import random

# write 'hello world' to the console
print('hello world')

# Initialize global scores
user_score = 0
computer_score = 0

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice: str, computer_choice: str) -> str:
    """Determine the winner of a round."""
    print(f"You chose: {user_choice}, Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user won"
    else:
        return "computer won"

def play_round():
    """Play a single round of rock, paper, scissors."""
    global user_score, computer_score

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        print("Invalid choice. Please try again.")

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "user won":
        print("You win this round!")
        user_score += 1
    elif winner == "computer won":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

def play_game():
    """Play the rock, paper, scissors game."""
    global user_score, computer_score

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_round()
        print(f"Scores -> You: {user_score}, Computer: {computer_score}")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ["yes", "no"]:  
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()