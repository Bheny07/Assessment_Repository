"""Adding on from v1 and making it, so it can accept inputs of 'y' and 'n
as well as 'yes or 'no'"""

# Ask the user if they have played the quiz before
response = input("Have you played the quiz before? Enter 'yes' or 'no': ")

# Check the user's response
if response.lower() in ["yes", "y"]:
    print("Welcome back!")
elif response.lower() in ["no", "n"]:
    print("Great, let's get started!")
else:
    print("Sorry, I didn't understand your response. Please enter 'yes' or "
          "'no'.")
