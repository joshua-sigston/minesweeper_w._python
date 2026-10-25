
# function will be command to use during game for user
def parse_input(string):
    parts = string.strip().lower().split()

    if not parts:
        return("Invalid", "Type a command.")

    command = parts[0]

    # 0, 0 are added to not throw an invalid error. game will just quit
    if command == "quit":
        return (command, 0 , 0)
    
    if len(parts) != 3:
        return ("Invalid", "Must enter 2 numbers. Example: '0 10' Please enter a blank line between numbers.")

    if command in ("flag", "check"):
        try:
            x = int(parts[1])
            y = int(parts[2])
            return (command, x, y)
        except ValueError:
            return ("Invalid", "Please enter a valid whole number")

    return ("Invalid", "Unknown Command")

# function takes user input to determine board size
def create_board_size(string):
    parts = string.strip().lower().split()

    if not parts:
        return("Invalid", "Type a command.")

    if len(parts) != 2:
        return ("Invalid", "Must enter 2 numbers. Example: '0 10' ")

    # converters to int or throws error
    try:
        rows = int(parts[0])
        cols = int(parts[1])
    except ValueError:
        print("Please enter 2 numbers")
        return ("Invalid", "Please enter valid numbers")

    # checks that number of cols and rows are both greater than 0
    if rows <=0 or cols <=0:
        return ("Invalid", "Please enter 2 numbers greater than 0")
    else:
        return (rows, cols)








# def test():
#     print("Enter command following this format: 'action_first number_second number' ")
#     line = input("> ")
#     parsed = parse_input(line)
    
#     r = int(parsed[0])
#     c = int(parsed[1])

# test()