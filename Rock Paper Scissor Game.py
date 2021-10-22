# A rock, paper, scissors game
# The expected output is below the code, which I will have to revisit in the future.

import random
import sys

myList = ["ROCK", "PAPER", "SCISSORS"]
response_rock, response_paper, response_scissors = ["r", "p", "s"]

print("\nROCK, PAPER, SCISSORS")
print("O Wins, 0 Losses, 0 Ties")
print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
user_input = input()

while True:
    print(user_input)
    random_hand = random.choices(myList, weights=None, k=1)  # random.choice(sequences[list/tuple name], weights
    # [possibility of each value, cum_weights[same, possibility is accumulated], k[an int defining the length of the
    # returned list]
    wins, losses, ties = [0, 0, 0]

    if user_input == "p":
        print("PAPER versus...\n" + str(random_hand))
        if str(random_hand) == "PAPER":
            print("It is a tie!")
            ties = ties + 1
        if str(random_hand) == "ROCK":
            print("You win!")
            wins = wins + 1
        if str(random_hand) == "SCISSORS":
            print("You lost!")
            losses = losses + 1
        break

    elif user_input == "r":
        print("ROCK versus...\n" + str(random_hand))
        if random_hand == "PAPER":
            print("You Lose!")
            losses = losses + 1
        if random_hand == "ROCK":
            print("It is a Tie!")
            ties = ties + 1
        if random_hand == "SCISSORS":
            print("You Win!")
            wins = wins + 1
        break

    elif user_input == "s":
        print("SCISSORS versus...\n" + str(random_hand))
        if random_hand == "PAPER":
            print("You Win!")
            wins = wins + 1
        if random_hand == "ROCK":
            print("You Lose!")
            losses = losses + 1
        if random_hand == "SCISSORS":
            print("It is a Tie!")
            ties = ties + 1
        break

    elif user_input == "q":
        sys.exit()
    else:
        print("You've entered the wrong entry\n" + str(random_hand))
    print("%ds Wins, %ds Losses, %ds Ties" % (wins, losses, ties))


"""
ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
p
PAPER versus...
PAPER
It is a tie!
0 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
s
SCISSORS versus...
PAPER
You win!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
"""
