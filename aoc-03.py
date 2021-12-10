from collections import defaultdict


def solution_part1(input_file):
    start_list = defaultdict(int)
    counter = 0
    with open(input_file) as file:
        for line in file:
            num = line.strip()
            counter += 1
            for i, j in enumerate(num):
                if j == '1':
                    start_list[i] += 1
    gamma = ''
    epsilon = ''
    for i in range(len(num)):
        ones = start_list[i]
        zeros = counter - ones
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(int(gamma, 2) * int(epsilon, 2))


def solution_part2(input_file):
    start_list = []
    with open(input_file) as file:
        for line in file:
            start_list.append(line.strip())
    tmp_list = start_list[:]
    for i in range(len(start_list[0])):
        new_list_zeros = []
        new_list_ones = []
        for num in tmp_list:
            if num[i] == '1':
                new_list_ones.append(num)
            else:
                new_list_zeros.append(num)
        if len(new_list_ones) >= len(new_list_zeros):
            tmp_list = new_list_ones
        else:
            tmp_list = new_list_zeros
        if len(tmp_list) == 1:
            break
    x = tmp_list[0]
    tmp_list = start_list[:]
    for i in range(len(start_list[0])):
        new_list_zeros = []
        new_list_ones = []
        for num in tmp_list:
            if num[i] == '1':
                new_list_ones.append(num)
            else:
                new_list_zeros.append(num)
        if len(new_list_ones) < len(new_list_zeros):
            tmp_list = new_list_ones
        else:
            tmp_list = new_list_zeros
        if len(tmp_list) == 1:
            break
    y = tmp_list[0]
    print(int(x, 2) * int(y, 2))


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-03-input/test-input.txt'
    real_input = 'aoc-03-input/real-input.txt'
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
