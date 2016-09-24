# File game_funcs.py
# Purpose: hold all our junk, for now

def play_game():
    game_score = 0
    valid_list = ["hit", "stand"]
    command = get_input(valid_list)
    if command == "stand":
        print("You stand at %d" % game_score)
        return
    else:
        pass #todo
    print("do gamestuff here")


def get_input(valid_list):
    while True:
        user_command = raw_input("Command: ")
        for test in valid_list:
            if user_command == test:
                return user_command
        print("Invalid command!  Please try again!")

