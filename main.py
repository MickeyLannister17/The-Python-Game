import random

while True:
    gameOptions = ["R","P", "S"]

    computer = random.choice(gameOptions)
    player = None
    print("******Welcome to the great game *******".upper())
    while player not in gameOptions:
    
        player = input("R, P, or S? Choose Wisely:\n").upper()
    if player == computer:

        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Loose!")
        if computer == "S":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hurray!You Win!")
    elif player == "P":
        if computer == "S":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You Loose!")
        if computer == "R":
            print("Computer: ",computer)
            print("Player: ",player)
            print("Hurray!You Win!")
            
        continueGame = input("Would You Like To continue The Game? (yes/no): ").lower()
        if continueGame != "yes":
            break
    
print("Goodbye!")    