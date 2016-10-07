# File game_flow.py
# Purpose: hold all our junk, for now

# io_user is overspecified in case we ever want io_filesystem or something
# for now, though, we can pretend it's our only io to make things easier
import io_user as io

# the foundational game loop
# if we want to track game win/losses, it needs to return a win/loss value
# to another loop above this one
# Also, currently no way to win, no opponent or anything
def play_game():
    game_score = 0
    valid_list = ["hit", "stand", "cheat"]
    while True:
        io.display("Your current score is %d"% game_score)
        command = io.get_command(valid_list)
        if command == "stand":
            io.display("You stand at %d" % game_score)
            return
        elif command == "cheat":
            io.display("What value would you like your score to be?")
            game_score = io.get_int()
            io.display("You've changed your score to %d"% game_score)
            if game_score > 21:
                io.display("You lose!")
                return
        else:
            val = 5 # todo randomize
            io.display("You are dealt a %d"% val)
            game_score += val 
            if game_score > 21:
                io.display("You bust at %d" % game_score)
                return



