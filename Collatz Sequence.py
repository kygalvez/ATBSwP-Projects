def collatz(number):
    while number != 1:
        if number % 2 == 0:
            print(number//2)
            return number//2
        else:
            print(3 * number + 1)
            return 3 * number + 1


user_number = int(input(print("Please enter an integer")))
collatz(user_number)
