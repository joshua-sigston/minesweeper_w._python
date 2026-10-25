from functions import *
from classes import *


def play_game():
    while True:
        print("Please enter a command with coordinates: ")
        line = input("> ")
        parsed = parse_input(line)

        if parsed[0] != "Invalid":
            return parsed

        print(parsed[1])

def start_game():
    while True:
        print("Please enter the number of rows and columns for your board (i.e. 10 10): ")
        line = input("> ")
        parsed = create_board_size(line)

        if parsed[0] != "Invalid":
            return parsed
        
        if parsed[0] == "Invalid":
            print(parsed[1])


def main():
    r, c = start_game()

    b = Board(r, c)
    # # print(b.create_mines())
    # # b.create_mines()
    b.display_board()


    while True:
        command, x, y = play_game()

        if command == "quit":
            break

        if command == "flag":
            b.toggle(x, y, command)
            b. display_board()




main()
    

