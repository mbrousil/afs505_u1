# Import from sys module
from sys import argv

# Get list of inputs
script, input_file = argv

# Define function for print whole file
def print_all(f):
    print(f.read())

# Define function to start at beginning of file
def rewind(f):
    f.seek(0)

# Define function to print one line at a time
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open file provided
current_file = open(input_file)

print("First let's print the whole file:\n")

# Print whole file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Go back to start
rewind(current_file)

print("Let's print three lines:")

# Print the first line
current_line = 1
print_a_line(current_line, current_file)
# current_line = 1

# Print next line
current_line += 1
print_a_line(current_line, current_file)
# current_line = 2

# Print next line
current_line += 1
print_a_line(current_line, current_file)
# current_line = 3
