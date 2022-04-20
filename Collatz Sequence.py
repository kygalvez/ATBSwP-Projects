def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
    print(number)


valid_input = False
while not valid_input:
    try:
        user_number = int(input("Please enter an integer: "))
        if user_number > 0:
            collatz(user_number)
            user_number = True
    except ValueError:
        print("must enter a positive number.")
