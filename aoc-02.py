def solution_part1(input_file):
    with open(input_file) as file:
        depth = 0
        horizontal = 0
        for line in file:
            a, b = str(line).split()
            if a == 'forward':
                horizontal += int(b)
            if a == 'down':
                depth += int(b)
            if a == 'up':
                depth -= int(b)
    print(depth * horizontal)


def solution_part2(input_file):
    with open(input_file) as file:
        aim = 0
        depth = 0
        horizontal = 0
        for line in file:
            a, b = str(line).split()
            if a == 'forward':
                horizontal += int(b)
                depth += aim * int(b)
            if a == 'down':
                aim += int(b)
            if a == 'up':
                aim -= int(b)
    print(depth * horizontal)


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-02-input/test-input.txt'
    real_input = 'aoc-02-input/real-input.txt'
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
