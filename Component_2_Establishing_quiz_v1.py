"""Asks the user to select a difficulty level for the quiz and returns the
level as an integer."""


def get_difficulty_level():
    while True:
        response = input("Select a difficulty level (1-3): ")
        if response.isdigit() and 1 <= int(response) <= 3:
            return int(response)
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


# Call the function to ask the user for the difficulty level
difficulty_level = get_difficulty_level()

# Use the value of difficulty_level to determine what to do next
print(f"You selected difficulty level {difficulty_level}. Let's start the "
      f"quiz!")
