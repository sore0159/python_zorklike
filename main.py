# File main.py
# Purpose: Program should be run from this file
# Goal: keep this file as clean as possible
#       import what we need from other files
import game_flow
import io_user


io_user.display("Welcome to Blackjack!\n")
game_flow.play_game()
io_user.display("Thanks for playing!  Goodbye!\n")


