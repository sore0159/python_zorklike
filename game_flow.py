# File game_flow.py
# Purpose: hold all our junk, for now

import io_user

# the foundational game loop
# if we want to track game win/losses, it needs to return a win/loss value
# to another loop above this one
# Also, currently no way to win, no opponent or anything
def play_game():
    game_score = 0
    valid_list = ["hit", "stand", "cheat"]
    while True:
        io_user.display("Your current score is %d"% game_score)
        command = io_user.get_command(valid_list)
        if command == "stand":
            io_user.display("You stand at %d" % game_score)
            return
        elif command == "cheat":
            game_score=int(input("What would you like your score to be?"))
            io_user.display("You've changed your score to %d"% game_score)
        else:
            val = 5 # todo randomize
            io_user.display("You are dealt a %d"% val)
            game_score += val 
            if game_score > 21:
                io_user.display("You bust at %d" % game_score)
                return



