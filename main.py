
def main():
    file_name = 'poker.txt'
    with open(file_name,'r') as games:
        #hands = games.read()
        #print("Player 1:{}\nPlayer 2:{}".format(hands[0:14], hands[15:29]))
        #hands = games.readline()
        #print(hands)
        data = []
        while games.readline():
            data.append(games.readline()[:-1])
        print(data[0])

    # run the functions defined above
if __name__ == "__main__":
	main()
