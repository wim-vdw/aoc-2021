def solution_part1(input_file):
    input_list = []
    max_x = 0
    max_y = 0
    with open(input_file) as file:
        for line in file:
            line = line.strip()
            start, end = line.split('->')
            x_start, y_start = map(int, start.split(','))
            x_end, y_end = map(int, end.split(','))
            if x_start > max_x:
                max_x = x_start
            if y_start > max_y:
                max_y = y_start
            if x_end > max_x:
                max_x = x_end
            if y_end > max_y:
                max_y = y_end
            if x_start == x_end or y_start == y_end:
                input_list.append((x_start, y_start, x_end, y_end))
    grid = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]
    for line in input_list:
        x_start = line[0]
        y_start = line[1]
        x_end = line[2]
        y_end = line[3]
        if x_start < x_end:
            for x in range(x_start, x_end + 1):
                grid[y_start][x] += 1
        if x_end < x_start:
            for x in range(x_end, x_start + 1):
                grid[y_start][x] += 1
        if y_start < y_end:
            for y in range(y_start, y_end + 1):
                grid[y][x_start] += 1
        if y_end < y_start:
            for y in range(y_end, y_start + 1):
                grid[y][x_start] += 1
    result = 0
    for line in grid:
        for element in line:
            if element >= 2:
                result += 1
    print(result)


def solution_part2(input_file):
    input_list = []
    max_x = 0
    max_y = 0
    with open(input_file) as file:
        for line in file:
            line = line.strip()
            start, end = line.split('->')
            x_start, y_start = map(int, start.split(','))
            x_end, y_end = map(int, end.split(','))
            if x_start > max_x:
                max_x = x_start
            if y_start > max_y:
                max_y = y_start
            if x_end > max_x:
                max_x = x_end
            if y_end > max_y:
                max_y = y_end
            input_list.append((x_start, y_start, x_end, y_end))
    grid = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]
    for line in input_list:
        x_start = line[0]
        y_start = line[1]
        x_end = line[2]
        y_end = line[3]
        if x_start == x_end or y_start == y_end:
            if x_start < x_end:
                for x in range(x_start, x_end + 1):
                    grid[y_start][x] += 1
            if x_end < x_start:
                for x in range(x_end, x_start + 1):
                    grid[y_start][x] += 1
            if y_start < y_end:
                for y in range(y_start, y_end + 1):
                    grid[y][x_start] += 1
            if y_end < y_start:
                for y in range(y_end, y_start + 1):
                    grid[y][x_start] += 1
        else:
            if x_start < x_end and y_start < y_end:
                x_tmp = x_start
                y_tmp = y_start
                while x_tmp <= x_end:
                    grid[y_tmp][x_tmp] += 1
                    x_tmp += 1
                    y_tmp += 1
            if x_start > x_end and y_start < y_end:
                x_tmp = x_start
                y_tmp = y_start
                while x_tmp >= x_end:
                    grid[y_tmp][x_tmp] += 1
                    x_tmp += -1
                    y_tmp += 1
            if x_start < x_end and y_start > y_end:
                x_tmp = x_start
                y_tmp = y_start
                while y_tmp >= y_end:
                    grid[y_tmp][x_tmp] += 1
                    x_tmp += 1
                    y_tmp += -1
            if x_start > x_end and y_start > y_end:
                x_tmp = x_start
                y_tmp = y_start
                while y_tmp >= y_end:
                    grid[y_tmp][x_tmp] += 1
                    x_tmp += -1
                    y_tmp += -1
    result = 0
    for line in grid:
        for element in line:
            if element >= 2:
                result += 1
    print(result)


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-05-input/test-input.txt'
    real_input = 'aoc-05-input/real-input.txt'
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
