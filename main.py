import random

print("Welcome to Rock Paper Scissors game!")
print("-----------------------------------")
while True:
    options = ["R","P","S"]

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("R, P, or S?: ").upper()


    if player == computer:
        print("computer:",(computer), "player:",(player))
        print("It's a Tie!")

    elif player == "R":
        if computer == "P":
            print("computer:",(computer), "player:",(player))
            print('computer wins')
        if computer == "S":
            print("computer:",(computer), "player:",(player))
            print('player wins')

    elif player == "S":
        if computer == "R":
            print("computer:",(computer), "player:",(player))
            print('computer wins')
        if computer == "P":
            print("computer:",(computer), "player:",(player))
            print('player wins')

    elif player == "P":
        if computer == "S":
            print("computer:",(computer), "player:",(player))
            print('computer wins')
        if computer == "R":
            print("computer:",(computer), "player:",(player))
            print('player wins')
        

    player_again = input("Wanna play again? (Y/N): ").upper()

    if player_again != "Y":
        break

print("Au-revoir!")