# Set up curly brace string for inserting text later
formatter = "{} {} {} {}"

# Print counting up in the braces
print(formatter.format(1, 2, 3, 4))
# Print counting up in text in the braces
print(formatter.format("one", "two", "three", "four"))
# Print True/False in the braces
print(formatter.format(True, False, False, True))
# Print the formatter text braces inside themselves
print(formatter.format(formatter, formatter, formatter, formatter))
# Print a four part message in the braces
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
