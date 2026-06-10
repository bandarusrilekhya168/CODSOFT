import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")

while True:

    user_choice = input(
        "\nChoose Rock, Paper, or Scissors: "
    ).lower()

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYour Choice: {user_choice}")
    print(f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    play_again = input(
        "\nPlay Again? (yes/no): "
    ).lower()

    if play_again != "yes":
        break

print("\nFinal Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
print("\nThank you for playing!")
