import random

print("\nI am thinking of a number between 1 and 20")

randNum = random.randint(1, 20)
i = 0
numOfGuesses = 0

while numOfGuesses < 6:
    print("Take a guess.")
    guess = int(input())

    if randNum > guess:
        print("Your guess is too low")
        numOfGuesses = numOfGuesses + 1
    elif randNum < guess:
        print("Your guess is too high")
        numOfGuesses = numOfGuesses + 1
    elif randNum == guess:
        numOfGuesses = numOfGuesses + 1
        break

print("Good job! You guessed my number in " + str(numOfGuesses) + " guesses!")
