"""Asking the user if they have played the quiz before"""

# Ask the user if they have played the quiz before
response = input("Have you played the quiz before? Enter 'yes' or 'no': ")

# Check the user's response
if response.lower() == "yes":
    print("Welcome back!")
elif response.lower() == "no":
    print("Great, let's get started!")
else:
    print("Sorry, I didn't understand your response. Please enter 'yes' or "
          "'no'.")

