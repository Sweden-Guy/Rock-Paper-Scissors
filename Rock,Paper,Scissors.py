import random

print("Please choose a hand: Rock, Paper or Scissors or R,P,S")

while True:
    choice = input().lower()
    list1 = ["Rock", "Paper", "Scissors"]

    if choice == "rock" or choice == "r":
        print("You chose: Rock")
        bot = random.choice(list1)
        print("The bot chose:", bot)

        if bot == "Rock":
            print("Draw!")
        elif bot == "Paper":
            print("Bot wins!")
        elif bot == "Scissors":
            print("You win!")

    elif choice == "paper" or choice == "p":
        print("You chose: Paper")
        bot = random.choice(list1)
        print("The bot chose:", bot)

        if bot == "Rock":
            print("You win!")
        elif bot == "Paper":
            print("Draw!")
        elif bot == "Scissors":
            print("Bot wins!")

    elif choice == "scissors" or choice == "s":
        print("You chose: Scissors")
        bot = random.choice(list1)
        print("The bot chose:", bot)

        if bot == "Rock":
            print("Bot wins!")
        elif bot == "Paper":
            print("You win!")
        elif bot == "Scissors":
            print("Draw!")

    else:
        print("Invalid choice! Please try again.")