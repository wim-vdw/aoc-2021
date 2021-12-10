def solution_part1(input_file):
    with open(input_file) as file:
        data = [int(x) for x in file.read().split(',')]
        min_pos, max_pos = min(data), max(data)
        result = max_pos * len(data)
        for pos in range(min_pos, max_pos):
            tmp = 0
            for position in data:
                tmp += abs(pos - position)
            if tmp < result:
                result = tmp
        print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        data = [int(x) for x in file.read().split(',')]
        min_pos, max_pos = min(data), max(data)
        result = 99999999999999999
        for pos in range(min_pos, max_pos):
            tmp = 0
            for position in data:
                delta = abs(pos - position)
                cost = 1
                tmp += (1 + delta) * delta // 2
            if tmp < result:
                result = tmp
            cost += 1
        print(result)


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-07-input/test-input.txt'
    real_input = 'aoc-07-input/real-input.txt'
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
