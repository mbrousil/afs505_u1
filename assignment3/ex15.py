# Import the argv function(?) from the sys package
from sys import argv

# Expect script and filename inputs from user
script, filename = argv

# Use filename input to open the file 
txt = open(filename)

# Note the empty space to the right of filename. It's cuz the user
# inputs text directly after the end of the prompt...so they'll
# run together if no space.
# filename = input("Please provide a filename ")

# txt = open(filename)


# Print the name of the file
print(f"Here's your file {filename}:")
# Print the contents of the file
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
