# 4. Rock, Paper Scissors Game

import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You win!")

    elif user == "paper" and computer == "rock":
        print("You win!")

    elif user == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
