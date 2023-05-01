"""Adding on from v2 and making it if response is 'no' or 'n' that it shows
the instructions to the user on how the quiz will work"""

# Ask the user if they have played the quiz before
response = input("Have you played the quiz before? Enter 'yes' or 'no': ")

# Check the user's response
if response.lower() in ["yes", "y"]:
    print("Welcome back, Select difficulty level")
elif response.lower() in ["no", "n"]:
    print("Great, let's get started!\nThis is a quiz on your knowledge of "
          "Maori numbers\nThese are the Instructions:\n1. Select your "
          "difficulty from 1-3 with 3 being the hardest.\n2. "
          "Answer the questions that are shown on screen. If you get it "
          "correct, it will say 'Correct' and if wrong it will say 'Wrong'.\n"
          "3. Continue on with the questions and get your final results once "
          "the quiz is finished.\n Lets play!")
else:
    print("Sorry, I didn't understand your response. Please enter 'yes' or "
          "'no'.")
