# A rock, paper, scissors game
# I have included the expected output is below the code.

import random
import sys


def get_user_input():
    user_input = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n")
    return user_input


myList = ["ROCK", "PAPER", "SCISSORS"]
response_rock, response_paper, response_scissors = ["r", "p", "s"]
wins, losses, ties = [0, 0, 0]

print("\nROCK, PAPER, SCISSORS")

while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    loser_input = get_user_input()
    random_hand = random.choice(myList)

    if loser_input == "p":
        print("PAPER versus...\n" + random_hand)
        if random_hand == "PAPER":
            print("It is a tie!")
            ties += 1
        if random_hand == "ROCK":
            print("You win!")
            wins += 1
        if random_hand == "SCISSORS":
            print("You lost!")
            losses += 1
    elif loser_input == "r":
        print("ROCK versus...\n" + str(random_hand))
        if random_hand == "PAPER":
            print("You Lose!")
            losses += 1
        if random_hand == "ROCK":
            print("It is a Tie!")
            ties += 1
        if random_hand == "SCISSORS":
            print("You Win!")
            wins += 1
    elif loser_input == "s":
        print("SCISSORS versus...\n" + str(random_hand))
        if random_hand == "PAPER":
            print("You Win!")
            wins += 1
        if random_hand == "ROCK":
            print("You Lose!")
            losses += 1
        if random_hand == "SCISSORS":
            print("It is a Tie!")
            ties += 1
    elif loser_input == "q":
        sys.exit()
    else:
        print(f"You've entered the wrong entry. Try again.\n")


# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!
# 1 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit

