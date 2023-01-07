import random

# Set up the game
options = ["rock", "paper", "scissors"]
score = 0

# Game loop
while True:
    choice = input("Enter rock, paper or scissors: ")
    computer_choice = random.choice(options)
    if choice == options:
        print("It's a tie")
    elif choice == "rock" and computer_choice == "scissors":
        print("You win")
        score += 1
    elif choice == "paper" and computer_choice == "rock":
        print("You win")
        score += 1
    elif choice == "scissors" and computer_choice == "paper":
        print("You win")
        score += 1
    else:
        print("You lose")
        score -= 1
    
    # Print the result
    print("Your chose: ", choice)
    print("Computer choice: ", computer_choice)
    print("Your score: ", score)

    play_again = input("Do you want to play again? (Y/N)")
    if play_again.lower() != "y":
        break

