import random
print("Rock, Paper, Scissors")
options = ["rock", "paper", "scissors"]
while True:
    player = input("Enter your choice [rock/paper/scissors]: ").lower()
    if player not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print(f"Computer chose {computer}.")

    if player == computer:
        print("It's a draw!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins.")

    play_again = input("Do you want to play again? [yes/no]: ").lower()
    if play_again == "no":
        break

print("Thanks for playing.")