import random

choices = ["rock", "paper", "scissors"]

print("Let's play Rock-Paper-Scissors!")
while True:
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if player_choice not in choices:
        print("Invalid input, please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"The computer chooses {computer_choice}.")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    
    while True:
        play_again = input("Play again? (y/n)").lower()
        if play_again == "y" or play_again == "n":
            break
        else:
            print("Invalid input, please try again.")
            
    if play_again == "n":
        break
