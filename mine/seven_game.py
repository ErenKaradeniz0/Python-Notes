import random
import time

def seven_game():
    def create_player_list():
        player_list = [*range(1, int(input("enter number of players :"))+1, 1)] #[1 2 3]
        for index in range(0, len(player_list)):
            player_list[index] = input("Enter player name : ") #[eren,ayşe,elif]
        return player_list

    
    player_list = create_player_list()
    number_of_players = len(player_list)

    # initialize first values
    for i in range(0, number_of_players):
        player_list_in = [*range(0, number_of_players, 1)] # num 3  [0,1,2]
        for index in range(0, number_of_players):
            player_list_in[index] = "player"+str(index+1)
    winner_not_found = True
    play_count = 0
    while (winner_not_found):
        for index in range(0, number_of_players): #0 1 2
            count = 0
            play_count += 1
            time.sleep(0.01)
            print(player_list_in[index], " : |", end=" ")
            for i in range(0, 3):
                number = random.randint(0, 9)
                print(number, end=" ")
                if (number == 7):
                    count += 1
            print("|")
            if (count > 2):
                print("\nTotal Play count : ", play_count)
                print("Play count of winner : ", play_count//number_of_players)
                print(player_list[index], "Wins !!!")
                winner_not_found = False
                break

seven_game()