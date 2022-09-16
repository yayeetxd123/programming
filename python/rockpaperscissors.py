import random
import time

running = True

player_score = 0
bot_score = 0

while running:

    player_1 = input("Player : rock/paper/scissors/quit: ")
    print("Bot is picking...")
    time.sleep(2)
    player_2 = random.choice(["rock", "paper", "scissors"])

    if player_1 == "rock" and player_2 == "rock":
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> tied <-----""".format(player_2))

    elif player_1 == "paper" and player_2 == "paper":
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> tied <-----""".format(player_2))

    elif player_1 == "scissors" and player_2 == "scissors":
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> tied <-----""".format(player_2))

    elif player_1 == "rock" and player_2 == "paper":
        bot_score += 1
        print("Current score : Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> Bot is the winner <-----""".format(player_2))

    elif player_1 == "rock" and player_2 == "scissors":
        player_score += 1
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> Player is the winner <-----""".format(player_2))

    elif player_1 == "paper" and player_2 == "rock":
        player_score += 1
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> Player is the winner <-----""".format(player_2))

    elif player_1 == "paper" and player_2 == "scissors":
        bot_score += 1
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> Bot is the winner <-----""".format(player_2))

    elif player_1 == "scissors" and player_2 == "rock":
        bot_score += 1
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> Bot is the winner <-----""".format(player_2))

    elif player_1 == "scissors" and player_2 == "paper":
        player_score += 1
        print("Current score: Bot - {} , Player - {}".format(bot_score, player_score))
        print("""Bot choice : {}
\n-----> Player is the winner <-----""".format(player_2))


    elif player_1 == "quit":
        break
    else:
        print("Invalid Operator!")

    print()
