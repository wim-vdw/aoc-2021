from copy import deepcopy


def solution_part1(input_file):
    with open(input_file) as file:
        dots_input_x = []
        dots_input_y = []
        folding_input = []
        for line in file:
            line = line.strip()
            if line.startswith('fold along'):
                folding_input.append(line.split('fold along ')[1])
            else:
                if line:
                    x, y = map(int, line.split(','))
                    dots_input_x.append(x)
                    dots_input_y.append(y)
    max_x = max(dots_input_x)
    max_y = max(dots_input_y)
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in zip(dots_input_x, dots_input_y):
        grid[y][x] = '#'
    first_fold_direction, first_fold_position = folding_input[0].split('=')
    first_fold_position = int(first_fold_position)
    new_grid = []
    if first_fold_direction == 'y':
        for y in range(first_fold_position):
            new_grid.append(deepcopy(grid[y]))
        new_y = 0
        for y in range(max_y, first_fold_position, -1):
            for x in range(max_x + 1):
                if grid[y][x] == '#':
                    new_grid[new_y][x] = '#'
            new_y += 1
    else:
        for y in range(max_y + 1):
            new_grid.append(deepcopy(grid[y][:first_fold_position]))
        for y in range(max_y + 1):
            new_x = 0
            for x in range(max_x, first_fold_position, -1):
                if grid[y][x] == '#':
                    new_grid[y][new_x] = '#'
                new_x += 1
    result = 0
    for line in new_grid:
        for char in line:
            if char == '#':
                result += 1
    print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        dots_input_x = []
        dots_input_y = []
        folding_input = []
        for line in file:
            line = line.strip()
            if line.startswith('fold along'):
                folding_input.append(line.split('fold along ')[1])
            else:
                if line:
                    x, y = map(int, line.split(','))
                    dots_input_x.append(x)
                    dots_input_y.append(y)
    max_x = max(dots_input_x)
    max_y = max(dots_input_y)
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in zip(dots_input_x, dots_input_y):
        grid[y][x] = '#'
    for fold_instruction in folding_input:
        fold_direction, fold_position = fold_instruction.split('=')
        fold_position = int(fold_position)
        new_grid = []
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1
        if fold_direction == 'y':
            for y in range(fold_position):
                new_grid.append(deepcopy(grid[y]))
            new_y = 0
            for y in range(max_y, fold_position, -1):
                for x in range(max_x + 1):
                    if grid[y][x] == '#':
                        new_grid[new_y][x] = '#'
                new_y += 1
        else:
            for y in range(max_y + 1):
                new_grid.append(deepcopy(grid[y][:fold_position]))
            for y in range(max_y + 1):
                new_x = 0
                for x in range(max_x, fold_position, -1):
                    if grid[y][x] == '#':
                        new_grid[y][new_x] = '#'
                    new_x += 1
        grid = deepcopy(new_grid)
    for line in grid:
        for char in line:
            print(char, sep='', end='')
        print()


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-13-input/test-input.txt'
    real_input = 'aoc-13-input/real-input.txt'
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
