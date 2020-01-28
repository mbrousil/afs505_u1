from sys import argv

script, filename = argv

file = open(filename)

print(f"Your file is named {filename}")
print(file.read())

file.close()
