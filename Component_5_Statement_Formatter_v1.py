"""Component 5 - Statement formatter 1"""

text = "Hello World"
sides = "$" * 3

formatted_text = f"{sides}{text}{sides}"
top_bottom = "*" * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
