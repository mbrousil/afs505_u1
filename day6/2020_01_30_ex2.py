def main():
    # argv is a global var so throw it in main()
    from sys import argv
    script, filename = argv

    # Define the file handle
    file_handle = open(filename)

    # Define open containers for iterated values
    line_count = 0
    word_count = 0
    char_count = 0

    # Define the first file line
    file_line = file_handle.readline()

    # While file lines can still be read (i.e., before end of file)
    while file_line:
        # Add one to line count
        line_count += 1

        # Add num chars in current line to line count
        char_count += len(file_line)

        # Add num words in current line to line count, counting num items in
        # list of split vals
        words = file_line.split(" ")
        word_count += len(words)

        # Read in next line
        file_line = file_handle.readline()

    # Report our findings
    print(line_count)
    print(word_count)
    print(char_count)
    print(filename)

main()

# 6 69 446 class_exercise_01_D06_data.txt is the answer
