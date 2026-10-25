
def parse_input(string):
    parts = string.strip().lower().split()

    if not parts:
        return("Invalid", "Type a command.")

    command = parts[0]

    if command in ("quit"):
        return (command, )
    
    if len(parts) != 3:
            return ("Invalid", "Must enter 2 numbers. Example: '0_10' ")

    if command in ("flag", "check"):
        x = int(parts[1])
        y = int(parts[2])
        return (command, x, y)

    return ("Invalid", "Uknown Command")

def start_game(string):
    parts = string.strip().lower().split()

    if not parts:
        return("Invalid", "Type a command.")

    if len(parts) != 2:
        return ("Invalid", "Must enter 2 numbers. Example: '0 10' ")

    return (parts[0], parts[1])

# def test():
#     print("Enter command following this format: 'action_first number_second number' ")
#     line = input("> ")
#     parsed = parse_input(line)
    
#     r = int(parsed[0])
#     c = int(parsed[1])

# test()