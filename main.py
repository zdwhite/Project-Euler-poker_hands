def parse_games(file_name):
    """ This fuction takes in a file name in the form of a .txt file
        With each poker game on a new line. It then returns a list
        Where each element in that list is a game of poker"""
    with open(file_name,'r') as games:
        #hands = games.read()
        #print("Player 1:{}\nPlayer 2:{}".format(hands[0:14], hands[15:29]))
        #hands = games.readline()
        #print(hands)
        data = []
        while games.readline():
            data.append(games.readline()[:-1])
        return data

def parse_players(games):
    """This function takes in a list of poker games
        Assigns a list of 5 cards to each player
        Then returns """
    player_1 = []
    player_2 = []
    for game in games:
        player_1.append(game[0:14])
        player_2.append(game[15:])
    return player_1, player_2

def main():
    file_name = 'poker.txt'
    games = parse_games(file_name)
    player_1,player_2 = parse_players(games)
    print(player_1[:5],"\n",player_2[:5])


    # run the functions defined above
if __name__ == "__main__":
	main()
