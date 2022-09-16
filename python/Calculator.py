print("Calculator: +, -, *, /, %, **.")

running = True

while running:

    first_number = int(input("Enter first number: "))
    operator = input("Enter operator/exit: ")
    second_number = int(input("Enter second number: "))
    total = 0
    print()

    if operator == "+":
        total = first_number + second_number
        print("-----> Sum: {} {} {} = {} <-----".format(first_number, operator, second_number, total))
        print()

    elif operator == "-":
        total = first_number - second_number
        print("-----> Subtraction: {} {} {} = {} <-----".format(first_number, operator, second_number, total))
        print()

    elif operator == "*":
        total = first_number * second_number
        print("-----> Multiplication: {} {} {} = {} <-----".format(first_number, operator, second_number, total))
        print()

    elif operator == "/":
        total = first_number // second_number
        print("-----> Division: {} {} {} = {} <-----".format(first_number, operator, second_number, total))
        print()

    elif operator == "%":
        total = first_number % second_number
        print("-----> Remainder: {} {} {} = {} <-----".format(first_number, operator, second_number, total))
        print()

    elif operator == "**":
        total = first_number ** second_number
        print("-----> Powered Number: {} {} {} = {} <-----".format(first_number, operator, second_number, total))
        print()

    elif operator == "exit" or "quit" or "break":
        running = False

    else:
        print("Invalid operator!")
        print("try again with different operator.")
