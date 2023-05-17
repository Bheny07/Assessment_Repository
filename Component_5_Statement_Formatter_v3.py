"""Component 5 - Statement formatter v3
Call function 4 times - once for each of the tests"""


# Function to format text output:
def formatter(symbol1, text1):
    sides = symbol1 * 3
    formatted_text = f"{sides}{text1}{sides}"
    top_bottom = symbol1 * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Maori Numbers Quiz"))
print()
print(formatter("!", "Correct"))
print()
print(formatter("x", "Incorrect, The Correct answer is: "))
print()
print(formatter("*", "Goodbye"))
print()
print(formatter("-", f"Your current score is: "))
print()
