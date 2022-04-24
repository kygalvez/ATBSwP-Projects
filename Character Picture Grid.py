# Copy grid list(below) and use it to print an image
# Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters.
# The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase
# going down.

# The directions for this project hinted on using a loop within a loop. However, as I was working on this project,
# I found that importing numpy and using the rot90 method was easier and faster.

import numpy as np


def print_grid(grid_list):  # Prints image from list of lists, with a for loop that is unpacked(*) in print statement
    for row in grid_list:
        print(*row)


def rotate_grid(before_grid):  # Rotates the unpacked list at a 90-degree angle
    after_grid = np.rot90(before_grid, 3)
    return after_grid


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print("\nBelow is the original list of lsits:")
print(grid)

print("\nBelow is the original grid:\n")
print_grid(grid)

print("\nBelow is the printed image rotated at a 90 degree angle:")
print_grid(rotate_grid(grid))
