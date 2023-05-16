"""Adding on from Component_4_Getting_User_Result_v2 and after the quiz is
completed, it gives the user the opportunity to play the quiz again"""

import random

# Define dictionaries of Maori numbers for each difficulty level
maori_numbers_level1 = {'tahi': 1, 'rua': 2, 'toru': 3, 'wha': 4, 'rima': 5,
                        'ono': 6, 'whitu': 7, 'waru': 8, 'iwa': 9, 'tekau': 10}

maori_numbers_level2 = {'tekau-ma-tahi': 11, 'tekau-ma-rua': 12,
                        'tekau-ma-toru': 13, 'tekau-ma-wha': 14,
                        'tekau-ma-rima': 15,
                        'tekau-ma-ono': 16, 'tekau-ma-whitu': 17,
                        'tekau-ma-waru': 18,
                        'tekau-ma-iwa': 19, 'rua tekau': 20}

maori_numbers_level3 = {'rua tekau ma tahi': 21, 'rua tekau ma rua': 22,
                        'rua tekau ma toru': 23, 'rua tekau ma wha': 24,
                        'rua tekau ma rima': 25, 'rua tekau ma ono': 26,
                        'rua tekau ma whitu': 27, 'rua tekau ma waru': 28,
                        'rua tekau ma iwa': 29, 'tekau ma tekau': 30}


# Define a function to generate a random question based on difficulty level
def generate_question(difficulty_level1):
    # Choose a random number from the appropriate dictionary
    if difficulty_level1 == 1:
        word = random.choice(list(maori_numbers_level1.keys()))
        answer1 = maori_numbers_level1[word]
    elif difficulty_level1 == 2:
        word = random.choice(list(maori_numbers_level2.keys()))
        answer1 = maori_numbers_level2[word]
    elif difficulty_level1 == 3:
        word = random.choice(list(maori_numbers_level3.keys()))
        answer1 = maori_numbers_level3[word]
    else:
        print("Invalid difficulty level. Please choose a difficulty "
              "level between 1 and 3.")
        return None, None

    # Return a tuple of the question and answer
    question1 = f"What number is {word}?"
    return question1, answer1


# Define a function to ask a question and get the user's answer
def ask_question(question2):
    # Print the question
    print(question2)
    # Get the user's answer
    user_answer1 = input("Enter your answer: ")
    # Return the user's answer
    return user_answer1


# Call the main function to run the quiz
if __name__ == '__main__':
    play_again = True

    while play_again:
        while True:
            # Get the difficulty level from the user
            difficulty_level = int(input("Choose a difficulty "
                                         "level (1, 2, or 3): "))
            if difficulty_level not in [1, 2, 3]:
                print("Invalid difficulty level. Please choose a "
                      "difficulty level between 1 and 3.")
                continue
            print(f"You selected difficulty level {difficulty_level}.")
            response = input("Would you like to start the quiz with this "
                             "difficulty level? (yes/no) ")
            if response.lower() in ["yes", "y"]:
                break

        # Set the number of questions based on the difficulty level
        if difficulty_level == 1:
            num_questions = 5
        elif difficulty_level == 2:
            num_questions = 5
        else:
            num_questions = 5

        # Initialize the score
        score = 0

        # Ask the specified number of questions
        for i in range(num_questions):
            # Generate a random question
            question, answer = generate_question(difficulty_level)
            # Ask the question and get the user's answer
            user_answer = ask_question(question)

            # Check if the user's answer is correct and update the score
            if int(user_answer) == answer:
                score += 1
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {answer}.")

            # Print the updated score
            print(f"Your current score is: {score}/{i + 1}")

        # Print the final score
        print(f"Your final score is: {score}/{num_questions} Congratulations")

        # Ask the user if they want to play again
        play_again_response = input("Would you like to play again? (yes/no) ")
        if play_again_response.lower() not in ["yes", "y"]:
            play_again = False
