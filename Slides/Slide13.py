import random
import time

# x, y, z = 42, 17, 25

# y < x and y <= z
# x % 2 == y % 2 or x % 2 == z % 2
# x <= y+z and x >= y+z
# not (x < y and x < z)
# (x+y) % 2 == 0 or not ((z-y) % 2 == 0)

# true false true true false


# print(both_odd(55, 1))


def seven_game():
    def create_player_list():
        player_list = [*range(1, int(input("enter number of players :"))+1, 1)]
        for index in range(0, len(player_list)):
            player_list[index] = input("Enter player name : ")
        return player_list

    player_list = create_player_list()

    # initialize first values
    for i in range(0, len(player_list)):
        player_list_in = [*range(0, len(player_list), 1)]
        for index in range(0, len(player_list_in)):
            player_list_in[index] = "player"+str(index+1)
    winner_not_found = True
    while (winner_not_found):
        for index in range(0, len(player_list)):
            count = 0
            # time.sleep(0.02)
            print(player_list_in[index], " : |", end=" ")
            for i in range(0, 3):
                number = random.randint(0, 9)
                print(number, end=" ")
                if (number == 7):
                    count += 1
            print("|")
            if (count > 2):
                print(player_list[index], "Wins !!!")
                winner_not_found = False
                break

            # for 3 rounds delete the break statement
            # break
            # if (player_list[index] == "Player1"):
            #     Player1 += 1
            # elif (player_list[index] == "Player2"):
            #     player2 += 1
            # elif (player_list[index] == "Player3"):
            #     player3 += 1
            # elif (player_list[index] == "Player4"):
            #     player4 += 1

            # if (Player1 > 2 or player2 > 2 or player4 > 2 or player3 > 2):
            #     print("Scores : \nPlayer1 : ", Player1, "\nPlayer2 : ", player2,
            #           "\nPlayer3 : ", player3, "\nPlayer4 : ", player4)
            #     break
        print()


seven_game()
