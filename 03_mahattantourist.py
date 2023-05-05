values_down = [[1, 2, 1, 0, 0], [1, 3, 2, 1, 1], [3, 0, 1, 0, 0], [2, 1, 0, 3, 0]]
values_right = [[1, 1, 0, 0], [0, 0, 0, 1], [3, 2, 1, 0], [3, 1, 2, 1], [3, 0, 2, 1]]
values_diagonal = [[3, 2, 1, 0], [0, 1, 1, 1], [2, 3, 0, 1], [2, 3, 0, 1]]


def manhattan(v, h, d, size_of_grid):           # v = down, h = right, d = diagonal
    grid = []
    for i in range(0, size_of_grid):         # fill empty grid with correct size
        grid.append([0] * size_of_grid)

    grid[0][0] = 0                            # fill first row and first column
    for i in range(1, size_of_grid):
        grid[i][0] = grid[i - 1][0] + v[i - 1][0]
    for j in range(1, size_of_grid):
        grid[0][j] = grid[0][j - 1] + h[0][j - 1]

    for i in range(1, size_of_grid):  # fill rest
        for j in range(1, size_of_grid):
            grid[i][j] = max(grid[i - 1][j] + v[i - 1][j], grid[i][j - 1] + h[i][j - 1],
                             grid[i - 1][j - 1] + d[i - 1][j - 1])

    print('The number of maximal attractions on your journey is:', grid[size_of_grid - 1][size_of_grid - 1])


if __name__ == '__main__':
    size_of_grid = len(values_right)  # length of values_right gives correct size of grid (5,5)
    manhattan(values_down, values_right, values_diagonal, size_of_grid)
