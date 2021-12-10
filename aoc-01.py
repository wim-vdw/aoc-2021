def solution_part1(input_file):
    with open(input_file) as file:
        first = True
        result = 0
        for measurement in file:
            current = int(measurement.strip())
            if first:
                previous = current
                first = False
            else:
                if previous < current:
                    result += 1
                previous = current
        print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        first = 0
        second = 0
        third = 0
        result = 0
        for measurement in file:
            current = int(measurement.strip())
            if not first:
                first = current
            elif first and not second and not third:
                second = current
            elif first and second and not third:
                third = current
            else:
                if first + second + third < second + third + current:
                    result += 1
                first, second, third = second, third, current
        print(result)


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-01-input/test-input.txt'
    real_input = 'aoc-01-input/real-input.txt'
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
