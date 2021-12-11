def increase(grid, grid_glow, x, y, first_run):
    did_glow = False
    if x < 0 or x == len(grid[0]):
        return False
    if y < 0 or y == len(grid):
        return False
    if grid[y][x] == 9:
        grid[y][x] = 0
        grid_glow[y][x] = True
        did_glow = True
    else:
        if grid[y][x] == 0:
            if first_run:
                grid[y][x] += 1
        else:
            grid[y][x] += 1
    return did_glow


def solution_part1(input_file):
    with open(input_file) as file:
        grid_input = [line.strip() for line in file]
    grid = [[int(x) for x in line] for line in grid_input]
    grid_max_x = len(grid[0])
    grid_max_y = len(grid)
    steps = 100
    result = 0
    for _ in range(steps):
        grid_glows = False
        grid_glow = [[False for _ in grid[0]] for _ in grid]
        for y in range(grid_max_y):
            for x in range(grid_max_x):
                result += increase(grid, grid_glow, x, y, True)
                if grid_glow[y][x]:
                    grid_glows = True
        while grid_glows:
            grid_glows = False
            for y in range(grid_max_y):
                for x in range(grid_max_x):
                    if grid_glow[y][x]:
                        grid_glow[y][x] = False
                        result += increase(grid, grid_glow, x - 1, y - 1, False)
                        result += increase(grid, grid_glow, x, y - 1, False)
                        result += increase(grid, grid_glow, x + 1, y - 1, False)
                        result += increase(grid, grid_glow, x - 1, y, False)
                        result += increase(grid, grid_glow, x + 1, y, False)
                        result += increase(grid, grid_glow, x - 1, y + 1, False)
                        result += increase(grid, grid_glow, x, y + 1, False)
                        result += increase(grid, grid_glow, x + 1, y + 1, False)
            for y in range(grid_max_y):
                for x in range(grid_max_x):
                    if grid_glow[y][x]:
                        grid_glows = True
    print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        grid_input = [line.strip() for line in file]
    grid = [[int(x) for x in line] for line in grid_input]
    grid_max_x = len(grid[0])
    grid_max_y = len(grid)
    result = 0
    all_together = False
    while not all_together:
        result += 1
        grid_glows = False
        grid_glow = [[False for _ in grid[0]] for _ in grid]
        for y in range(grid_max_y):
            for x in range(grid_max_x):
                _ = increase(grid, grid_glow, x, y, True)
                if grid_glow[y][x]:
                    grid_glows = True
        while grid_glows:
            grid_glows = False
            for y in range(grid_max_y):
                for x in range(grid_max_x):
                    if grid_glow[y][x]:
                        grid_glow[y][x] = False
                        _ = increase(grid, grid_glow, x - 1, y - 1, False)
                        _ = increase(grid, grid_glow, x, y - 1, False)
                        _ = increase(grid, grid_glow, x + 1, y - 1, False)
                        _ = increase(grid, grid_glow, x - 1, y, False)
                        _ = increase(grid, grid_glow, x + 1, y, False)
                        _ = increase(grid, grid_glow, x - 1, y + 1, False)
                        _ = increase(grid, grid_glow, x, y + 1, False)
                        _ = increase(grid, grid_glow, x + 1, y + 1, False)
            for y in range(grid_max_y):
                for x in range(grid_max_x):
                    if grid_glow[y][x]:
                        grid_glows = True
        all_together = True
        for y in range(grid_max_y):
            for x in range(grid_max_x):
                if grid[y][x] != 0:
                    all_together = False
    print(result)


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-11-input/test-input.txt'
    real_input = 'aoc-11-input/real-input.txt'
    print('***** Part 1 TEST run *****')
    solution_part1(test_input)
    if real_run:
        print('***** Part 1 REAL run *****')
        solution_part1(real_input)
    print('***** Part 2 TEST run *****')
    solution_part2(test_input)
    if real_run:
        print('***** Part 2 REAL run *****')
        solution_part2(real_input)
