
# Function to ask if User has played the quiz before
def quiz_played_before():
    response1 = input("Have you played the quiz before? Enter 'yes' or 'no': ")

    if response1.lower() in ["yes", "y"]:
        return True
    elif response1.lower() in ["no", "n"]:
        print("Great, let's get started!\nThis is a quiz on your knowledge of"
              " Maori numbers\nThese are the Instructions:\n1. Select your "
              "difficulty from 1-3 with 3 being the hardest.\n2. "
              "Answer the questions that are shown on screen. If you get it "
              "correct, it will say 'Correct' and if wrong it will say 'Wrong'"
              "\n""3. Continue on with questions and get your final results"
              " once the quiz is finished.\n Lets play!")
        return False
    else:
        print("Sorry, I didn't understand your response. "
              "Please enter 'yes' or 'no'.")
        # Call the function recursively until a valid response is entered
        return quiz_played_before()


def get_difficulty_level():
    while True:
        response1 = input("Select a difficulty level (1-3): ")
        if response1.isdigit() and 1 <= int(response1) <= 3:
            return int(response1)
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


# Call the function to ask the user if they have played the quiz before
played_before = quiz_played_before()

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
