import random
import time
from traceback import print_tb

# x, y, z = 42, 17, 25

# y < x and y <= z
# x % 2 == y % 2 or x % 2 == z % 2
# x <= y+z and x >= y+z
# not (x < y and x < z)
# (x+y) % 2 == 0 or not ((z-y) % 2 == 0)

# true false true true false


# print(both_odd(55, 1))


def seven_game(player_list):
    #initialize first values
    Player1, player2, player3, player4 = 0, 0, 0, 0
    while (True):
        # index = random.randint(0, 3)
        for index in range(0, 4):
            count = 0
            # time.sleep(0.5)
            print(player_list[index], " : |", end=" ")
            for i in range(0, 3):
                number = random.randint(0, 8)
                print(number, end=" ")
                if (number == 7):
                    count += 1
            print("|")

        if (count > 2):
            print(player_list[index], "Wins !!!")
            print()
            # for 3 rounds delete the break statement
            break
            if (player_list[index] == "Player1"):
                Player1 += 1
            elif (player_list[index] == "Player2"):
                player2 += 1
            elif (player_list[index] == "Player3"):
                player3 += 1
            elif (player_list[index] == "Player4"):
                player4 += 1

            if (Player1 > 2 or player2 > 2 or player4 > 2 or player3 > 2):
                print("Scores : \nPlayer1 : ", Player1, "\nPlayer2 : ", player2,
                      "\nPlayer3 : ", player3, "\nPlayer4 : ", player4)
                break
        print()


player_list = ["eren","şevval","enes","miray"]

seven_game(player_list)
