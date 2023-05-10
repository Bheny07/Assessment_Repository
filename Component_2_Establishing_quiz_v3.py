"""Adding on from v2 by changing the code so that the code is able to
correspond with the establishing quiz code so that the user is able to select
the difficulty level they want to play with and is abe to play the quiz"""

while True:
    difficulty_level = int(input("Choose a difficulty level (1, 2, or 3): "))
    print(f"You selected difficulty level {difficulty_level}.")
    response = input("Would you like to start the quiz with this difficulty"
                     " level? (yes/no) ")
    if response.lower() in ["yes", "y"]:
        break
    elif response.lower() in ["no", "n"]:
        print("Okay, let's try again.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

