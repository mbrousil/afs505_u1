"""A Python script that runs Conway's Game of Life.

..module::game_of_life
    :synopsis: This script runs a version of Conway's Game of Life. It takes
        command line inputs from the user, including the number of time points
        to run for and the starting cells to turn on and produces a visualization
        of the game.

..moduleauthor:: Matthew Brousil
..modulereviewer:: Brian Eisenbarth
..modulescore:: 99/100

"""

def main():
    """Runs the Game of Life, requiring no inputs.

    :return: prints the string contents of a 2D list joined to create a grid.

    """

    from sys import argv

    # Store the number of runs to go for
    runs = int(argv[1])

    # Store the user's requested "on" cell locations as text
    user_inputs = argv[2:len(argv)]

    for text_pair in range(len(user_inputs)):
        # Split the "on" cell coordinates into pairs
        user_inputs[text_pair] = user_inputs[text_pair].split(sep = ":")

        # For each coordinate item in the pair...
        for number in range(len(user_inputs[text_pair])):
            # Convert the coordinate item into an integer
            user_inputs[text_pair][number] = int(user_inputs[text_pair][number])

    # Initiate the grid (all "OFF"):
    # Note that you need to initiate this way cuz not using range creates 30 lists
    # with identical identifiers under the hood, so python thinks you want to modify
    # them ALL at once in the future...
    initial_grid = [["-"] * 80 for initiated_row in range(30)]

    # Place the user's ON cells row by column:
    for on_pair in range(len(user_inputs)):

        # Define row location of cell
        row_to_turn = user_inputs[on_pair][0]
        # Define column location of cell
        col_to_turn = user_inputs[on_pair][1]

        # Redefine cell value to be "on"
        initial_grid[row_to_turn][col_to_turn] = "X"

    # For the list corresponding to this row
    for row_list in range(len(initial_grid)):
        # Join it into one string
        initial_grid[row_list] = "".join(initial_grid[row_list])

    # Create a grid using line breaks with each row list
    initial_grid_joined = "\n".join(initial_grid)
    # Visualize it
    print(initial_grid_joined)

    # Function to return the number of "ON" neighbor cells:
    def test_surroundings(cell, row, grid):
        """Tests for the number of neighbors that are "on" for a given cell location.

        Takes row and cell index (i.e. column) as input and calculates the number
        of neighbors in all directions that are considered "on" by detecting the
        number of "X" characters in all adjacent cells.

        :param cell: The column number/cell index of the character of interest
        for a given row.
        :type cell: An integer value.

        :param row: The row number of the character of interest.
        :type row: An integer value.

        :param grid: The variable containing the grid list for the game.
        :type grid: A 2D list .

        :return: A single integer sum value for all "on" neighboring cells.
        :rtype: An integer value.

        """

        # If first cell in the row
        if cell == 0:
            # And first row of the grid
            if row == 0:
                # Count the total corresponding cells that are "X"
                sum_on = grid[row][(cell + 1)].count("X") + grid[row + 1][(cell):(cell + 2)].count("X")
            # Not first or last row of grid
            elif (row > 0 and row < (len(grid) - 1)):
                # Count the total corresponding cells that are "X"
                sum_on = grid[row - 1][cell:(cell + 2)].count("X") + grid[row][(cell + 1)].count("X") + grid[row + 1][cell:(cell + 2)].count("X")
            # Last row of grid
            elif row == (len(grid) - 1):
                # Count the total corresponding cells that are "X"
                sum_on = grid[row - 1][cell:(cell + 2)].count("X") + grid[row][(cell + 1)].count("X")

        # If not first cell in the row or last
        elif (cell > 0 and cell < (len(grid[row]) - 1)):
            # And first row of the grid
            if row == 0:
                # Count the total corresponding cells that are "X"
                sum_on = grid[row][(cell - 1)].count("X") + grid[row][(cell + 1)].count("X") + grid[row + 1][(cell - 1):(cell + 2)].count("X")
            # Not first or last row of grid
            elif (row > 0 and row < (len(grid) - 1)):
                # Count the total corresponding cells that are "X"
                sum_on = grid[row - 1][(cell - 1):(cell + 2)].count("X") + grid[row][(cell - 1)].count("X") + grid[row][(cell + 1)].count("X") + grid[row + 1][(cell - 1):(cell + 2)].count("X")

            # Last row of grid
            elif row == (len(grid) - 1):
                # Count the total corresponding cells that are "X"
                sum_on = grid[row - 1][(cell - 1):(cell + 2)].count("X") + grid[row][(cell - 1)].count("X") + grid[row][(cell + 1)].count("X")

        # If it's the last cell in the row
        elif cell == (len(grid[row]) - 1):
            # And first row of the grid
            if row == 0:
                # Count the total corresponding cells that are "X"
                sum_on = grid[row][(cell - 1)].count("X") + grid[row + 1][(cell - 1):cell].count("X")
            # Not first or last row of grid
            elif (row > 0 and row < (len(grid) - 1)):
                # Count the total corresponding cells that are "X"
                sum_on = grid[row - 1][(cell - 1):cell].count("X") + grid[row][(cell - 1)].count("X") + grid[row + 1][(cell - 1):cell].count("X")
            # Last row of grid
            elif row == (len(grid) - 1):
                # Count the total corresponding cells that are "X"
                sum_on = grid[row - 1][(cell - 1):cell].count("X") + grid[row][(cell - 1)].count("X")

        return(sum_on)

    # Initiate counter for current run (or "tick")
    current_run = 1

    # As long as the current run is not more than the user's specified number of runs...
    while current_run <= runs:

        # print(current_run)

        # A dictionary that will track all decisions (i.e., change/keep as-is) for all cells of the grid
        all_cell_decisions = {}

        # A loop that makes decisions about changing the status of each cell in each row
        # Generates a dictionary with a new dictionary for each row
        for row in range(len(initial_grid)):

            # A new row created to replace the current row, with dummy vals
            new_row = ["0"] * 80

            # For each cell in this row of the grid...
            for char in range(len(initial_grid[row])):

                # Count the number of "on" neighbors
                neighbors_on = test_surroundings(cell = char, row = row, grid = initial_grid)
                # Currently OFF & DON'T turn on:
                if ((neighbors_on != 3) & (initial_grid[row][char] == "-")):
                    # Cell is off
                    new_row[char] = "-"
                # Currently OFF & DO turn on:
                elif ((neighbors_on == 3) & (initial_grid[row][char] == "-")):
                    # Cell is on
                    new_row[char] = "X"
                # Currently ON & DO keep on:
                elif ((neighbors_on == 2 or neighbors_on == 3) & (initial_grid[row][char] == "X")):
                    # Cell is on
                    new_row[char] = "X"
                # Currently ON & DON'T keep on:
                elif ((neighbors_on < 2 or neighbors_on > 3) & (initial_grid[row][char] == "X")):
                    # Cell is off
                    new_row[char] = "-"

            # Tack the current row's decisions on to the decision dictionary
            all_cell_decisions.update({row: new_row})

        # Rebuild the initial grid from the values in the decisions dictionary
        initial_grid = list(all_cell_decisions.values())

        # Collapse each row's list to a single string:
        for row_list in range(len(initial_grid)):
            # Join it into one string
            initial_grid[row_list] = "".join(initial_grid[row_list])
        # Join the full grid into one string with line breaks
        initial_grid_joined = "\n".join(initial_grid)
        # Visualize it
        print(initial_grid_joined)

        current_run += 1

main()
