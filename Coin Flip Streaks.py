# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated
# list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of
# randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this
# code in a loop that repeats the experiment 10,000 times, so we can find out what percentage of the coin flips contain
# a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50%
# of the time and a 1 value the other 50% of the time

import random
number_of_streaks = 0
repeat_runs = 10000
for experiment_number in range(repeat_runs):

    # code that creates a list of 100 'heads' or 'tails values.
    number_flips = 10
    coin_list = []  # empty list to collect the simulation results per run
    for i in range(number_flips):
        if random.randint(0, 1) == 0:  # 0 - heads, 1 - tails
            coin_list.append("heads")
        else:
            coin_list.append("tails")

    # code that checks if there is a streak of 6 heads or tails in a row
    coin_string = ""  # an empty string for the coin_list to string conversion
    for j in coin_list:
        coin_string += j
    if "headsheadsheadsheadsheadsheads" in coin_string or "tailstailstailstailstailstails" in coin_string:
        number_of_streaks += 1
    print("List of randomly selected data list: ", coin_list)
print("\nChance of streak %.2f%%" % (number_of_streaks / 100))
