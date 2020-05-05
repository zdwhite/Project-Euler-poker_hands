
def main():
    file_name = 'poker.txt'
    with open(file_name,'r') as games:
        hands = games.readall()
        print(hands)

    # run the functions defined above
if __name__ == "__main__":
	main()
