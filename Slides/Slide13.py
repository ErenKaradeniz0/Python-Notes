import random

# x, y, z = 42, 17, 25

# y < x and y <= z
# x % 2 == y % 2 or x % 2 == z % 2
# x <= y+z and x >= y+z
# not (x < y and x < z)
# (x+y) % 2 == 0 or not ((z-y) % 2 == 0)

# true false true true false


# print(both_odd(55, 1))



def seven_game(Names):
    Player1, player2, player3, player4 = 0, 0, 0, 0
    while (True):
        count = 0
        index = random.randint(0, 3)
        print(Names[index], " : ", end=" ")
        for i in range(1, 11):
            number = random.randint(1, 31)
            print(number, end=" ")
            if (number == 7):
                print(Names[index], "Wins !!!")
                count += 1

        if (count > 2):
            print("\n")
            print(Names[index], "Wins !!!")
            print()
            if (Names[index] == "Player1"):
                Player1 += 1
            elif (Names[index] == "Player2"):
                player2 += 1
            elif (Names[index] == "Player3"):
                player3 += 1
            elif (Names[index] == "Player4"):
                player4 += 1

            if (Player1 > 2 or player2 > 2 or player4 > 2 or player3 > 2):
                print("Scores : \nPlayer1 : ", Player1, "\nPlayer2 : ", player2,
                      "\nPlayer3 : ", player3, "\nPlayer4 : ", player4)
                break
        print()


Names = ["Player1", "Player2", "Player3", "Player4"]

seven_game(Names)
