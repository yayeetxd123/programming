import random

secret_number = random.randint(1,10)
guess = ""
curr_tries = 3
total_tries = 0

while curr_tries > total_tries:
    print("You have {} tries left".format(curr_tries))
    guess = int(input("Enter Number: "))

    if guess != secret_number:
        curr_tries -= 1

        if curr_tries >= 1:
            print("Try Again!")
        else:
            print("Game Over! You ran out of tries!")

    elif guess == secret_number:
        print("Nice, You Won!")
        break
