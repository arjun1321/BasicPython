import random

comGuess = random.randint(0,100)

while True:
    userGuess = int(input("Guess a number between 0-100:"))

    if userGuess > comGuess:
        print("Guess lower")
    elif userGuess < comGuess:
        print("Guess Higher")
    else:
        print("Congrats, you've guessed the correct number")
        break