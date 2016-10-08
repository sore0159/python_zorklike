# File io_user.py 
# Purpose: 
#       handle displaying information to the user
#       handle passing input from user to program
# Parsing and validation are uncertain in-between io and game logic


# maybe more later
def display(text):
    print(text)

# not a very flexible tool, but it works
def get_command(valid_list):
    while True:
        user_command = input("Command: ")
        for test in valid_list:
            if user_command == test:
                return user_command
        print("Invalid command!  Please try again!")
        print("Valid commands are: "+", ".join(valid_list))


# possible additions: 
#       a way for the user to cancel?  If so, all calls to this function must check and handle user cancels.  May be better to have a separate cancellable function.
#       sometimes redisplaying the original prompt, which a user might forget after enough failed entries
def get_int():
    while True:
        user_input = input("Value: ")
        try:
            val = int(user_input) # I still don't quite trust int(x) as a conversion tool, but it seems the way to go
        except ValueError:
            print("Please enter a valid number!")
        else:
            return val
