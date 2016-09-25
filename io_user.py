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

