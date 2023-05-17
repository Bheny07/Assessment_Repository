"""Component 5 - Statement formatter v2
Changing v1 into a function"""


# Function to format text output:
def formatter(symbol1, text1):
    sides = symbol1 * 3
    formatted_text = f"{sides}{text1}{sides}"
    top_bottom = symbol1 * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
text = input("Enter the statement you want to format: ")
symbol = input("What symbol do you want to use: ")
print()
print(formatter(symbol, text))
