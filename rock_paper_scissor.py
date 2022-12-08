import random
while True:

    choices= ["rock","paper","scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock , Paper or Scissor?: ")

    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("Tie")
    
    elif player == 'Rock':
        if computer == 'Paper':
            print("computer:", computer)
            print("player:", player)
            print("You Loose!")
        if computer == 'Scissor':
            print("computer:", computer)
            print("player:", player)
            print("You Win!")
    elif player == 'Paper':
        if computer == 'Rock':
            print("computer:", computer)
            print("player:", player)
            print("You Win!")
        if computer == 'Scissor':
            print("computer:", computer)
            print("player:", player)
            print("You Loose!")
    elif player == 'Scissor':
        if computer == 'Rock':
            print("computer:", computer)
            print("player:", player)
            print("You Win!")
        if computer == 'Paper':
            print("computer:", computer)
            print("player:", player)
            print("You Loose!")

    play_again = input("Play again? (yes/no): ")

    if play_again != "yes":
        break
print("Bye!")




