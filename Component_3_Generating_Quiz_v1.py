"""Establishing the quiz so that a random generated question on Maori
numbers will be shown to the user"""

import random

# Define a dictionary of Maori numbers from 1-10
maori_numbers = {'tahi': 1, 'rua': 2, 'toru': 3, 'wha': 4, 'rima': 5, 'ono': 6,
                 'whitu': 7, 'waru': 8, 'iwa': 9, 'tekau': 10}


# Define a function to generate a random question
def generate_question():
    # Choose a random number from 1-10
    word = random.choice(list(maori_numbers.keys()))
    # Get the Maori word for that number
    answer1 = maori_numbers[word]
    # Return a tuple of the question and answer
    question2 = f"What number is {word}?"
    return question2, answer1


# Define a function to ask a question and get the user's answer
def ask_question(question1):
    # Print the question
    print(question1)


# Call the main function to run the quiz
if __name__ == '__main__':
    num_questions = 1
    for i in range(num_questions):
        # Generate a random question
        question, answer = generate_question()
        # Ask the question and get the user's answer
        ask_question(question)
