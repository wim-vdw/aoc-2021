from collections import Counter


def generate(template, pair_insertions):
    new_list = [template[0]]
    for i in range(1, len(template)):
        pair = template[i - 1:i + 1]
        if pair in pair_insertions:
            new_list.append(pair_insertions[pair])
        new_list.append(pair[1])
    return ''.join(new_list)


def solution_part1(input_file):
    with open(input_file) as file:
        pair_insertions = {}
        for line_num, line in enumerate(file):
            line = line.strip()
            if line_num == 0:
                template = line
            elif line:
                pair, insertion = line.split(' -> ')
                pair_insertions[pair] = insertion
    new_template = template
    for _ in range(10):
        new_template = generate(new_template, pair_insertions)
    counter = Counter(new_template)
    most_common = counter.most_common()[0]
    least_common = counter.most_common()[-1]
    print(most_common[1] - least_common[1])


def solution_part2(input_file):
    pass


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-14-input/test-input.txt'
    real_input = 'aoc-14-input/real-input.txt'
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
