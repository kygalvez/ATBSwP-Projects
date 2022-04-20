def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    print(number)


user_number = int(input("Please enter an integer: "))
collatz(user_number)
