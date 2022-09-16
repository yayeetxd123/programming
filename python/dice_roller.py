import random
import time

while True:
    choice = str(input("Type 'r' to roll the dice or 'e' to exit: "))
    if choice == "r":
        print("Rolling the dice...")
        a = random.randint(1,6)
        time.sleep(1)
        print("Your number: {}".format(a))
    elif choice == "help":
        print("""r - roll
e - exit""")
    elif choice == "e":
        print("Thanks for using my dice")
        break
