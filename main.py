import random

print("Welcome to Rock Paper Scissors game!")
print("-----------------------------------")
while True:
    choices = ["R","P","S"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("R, P, or S?: ").upper()


    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("It's a Tie!")

    elif player == "R":
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("Sorry You lose!")
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("Bingo You win!")

    elif player == "S":
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("Sorry You lose!")
        if computer == "P":
            print("computer: ", computer)
            print("player: ", player)
            print("Bingo You win!")

    elif player == "P":
        if computer == "S":
            print("computer: ", computer)
            print("player: ", player)
            print("Sorry You lose!")
        if computer == "R":
            print("computer: ", computer)
            print("player: ", player)
            print("Bingo You win!")
        

    player_again = input("Wanna play again? (Y/N): ").upper()

    if player_again != "Y":
        break

print("Au-revoir!")