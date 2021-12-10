def solution_part1(input_file):
    with open(input_file) as file:
        data = [int(x) for x in file.read().split(',')]
        days = 80
        for day in range(1, days + 1):
            new_fish = 0
            for counter, value in enumerate(data):
                if value == 0:
                    data[counter] = 6
                    new_fish += 1
                else:
                    data[counter] -= 1
            for _ in range(new_fish):
                data.append(8)
        print(len(data))


def solution_part2(input_file):
    with open(input_file) as file:
        data = [int(x) for x in file.read().split(',')]
        result = [0 for _ in range(9)]
        for fish in data:
            result[fish] += 1
        days = 256
        for day in range(1, days + 1):
            new_8 = result[0]
            new_7 = result[8]
            new_6 = result[7] + result[0]
            new_5 = result[6]
            new_4 = result[5]
            new_3 = result[4]
            new_2 = result[3]
            new_1 = result[2]
            new_0 = result[1]
            result[0] = new_0
            result[1] = new_1
            result[2] = new_2
            result[3] = new_3
            result[4] = new_4
            result[5] = new_5
            result[6] = new_6
            result[7] = new_7
            result[8] = new_8
        print(sum(result))


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-06-input/test-input.txt'
    real_input = 'aoc-06-input/real-input.txt'
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
