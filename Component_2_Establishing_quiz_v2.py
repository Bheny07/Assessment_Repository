"""Adding on from v1 by giving the user the chance to continue on with the
difficulty level they selected or giving the user an option to change. and also
adding to the code so that it can accept 'y' or 'n' as well as 'yes' or 'no'"""


def get_difficulty_level():
    while True:
        response1 = input("Select a difficulty level (1-3): ")
        if response1.isdigit() and 1 <= int(response1) <= 3:
            return int(response1)
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


# Prompt the user to select a difficulty level
print("Welcome to the quiz!")
while True:
    difficulty_level = get_difficulty_level()
    print(f"You selected difficulty level {difficulty_level}.")
    response = input("Would you like to start the quiz with this difficulty "
                     "level? (yes/no) ")
    if response.lower() in ["yes", "y"]:
        break
    elif response.lower() in ["no", "n"]:
        print("Okay, let's try again.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Starting the quiz...")
