import random

while True:
    user_action = input(str("Enter a choice (rock(R), paper(P), scissors(S)): "))
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    if user_action == possible_actions:
        print(f"\nPlayer({user_action}) : CPU ({computer_action}).\n")
        print(f"Both players selected {user_action}. It's a tie!")
        if user_action == "R":
            while computer_action == "scissors":
                print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        if user_action == "P":
            while computer_action == "rock":
                print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        if user_action == "S":
            while computer_action == "paper":
                print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
    else:
        if user_action != computer_action:
            print("INVALID OPTION Try Again")
        user_action = input(str("Enter a choice (rock(R), paper(P), scissors(S)): "))
