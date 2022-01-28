#  This program prints a zigzag pattern that goes back and forth until the user/programmer interrupts the program

import sys


def running_zigzag(n):
    try:
        while True:  # will run program until user stops(ctrl-c) the program
            for i in range(n):  # first set of for loops that prints zigzag going towards the right
                for j in range(0, i):
                    print(" ", end="")
                for k in range(0, n):
                    print("*", end="")
                print("\r")
            for z in range(n, 0, -1): # first set of for loops that prints zigzag going towards the left
                for m in range(0, z):
                    print(" ", end="")
                for p in range(0, n):
                    print("*", end="")
                print("\r")
    except KeyboardInterrupt:
        sys.exit()


running_zigzag(8)
