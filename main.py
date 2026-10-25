from functions import *
from classes import *


def play_game():
    print("Please enter a command with coordinates: ")
    line = input("> ")
    parsed = parse_input(line)
    return parsed

def main():
    print("Please enter the number of rows and columns for your board (i.e. 10_10): ")
    line = input("> ")
    parsed = start_game(line)

    r = int(parsed[0])
    c = int(parsed[1])

    b = Board(r, c)
    b.create_board()
    b.display_board()

    command = play_game()
    print(command[0])
    x = command[1]
    y = command[2]

    if command[0] == "flag":
        b.toggle(x, y, command[0])
        b. display_board()




main()
    

