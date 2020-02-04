def iteration_function(start, stop, increment):

    i = start
    numbers = []

    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

iteration_function(start = 1, stop = 10, increment = 2)

def loop_iteration_function(start, stop, increment):

    print("This is a new function, which uses a for loop.")

    i = start
    numbers = []

    for i in range(start, stop, increment):
        print(i)

loop_iteration_function(start = 1, stop = 10, increment = 2)

def loop_iteration_no_inc(start, stop):

    print("This is a new function, which uses a for loop.")

    i = start
    numbers = []

    for i in range(start, stop):
        print(i)

loop_iteration_no_inc(start = 1, stop = 10)
