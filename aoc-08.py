def solution_part1(input_file):
    with open(input_file) as file:
        result = 0
        for line in file:
            line = line.strip()
            signal_patterns, output = line.split('|')
            output = output.strip()
            output = [x for x in output.split(' ')]
            for num in output:
                if len(num) in (2, 3, 4, 7):
                    result += 1
        print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        result = 0
        for line in file:
            line = line.strip()
            signal_patterns, output = line.split('|')
            signal_patterns = signal_patterns.strip()
            output = output.strip()
            signal_patterns = [set(x) for x in signal_patterns.split(' ')]
            output = [set(x) for x in output.split(' ')]
            codes = {}
            for signal in signal_patterns:
                if len(signal) == 2:
                    codes[1] = signal
            for signal in signal_patterns:
                if len(signal) == 3:
                    codes[7] = signal
            for signal in signal_patterns:
                if len(signal) == 4:
                    codes[4] = signal
            for signal in signal_patterns:
                if len(signal) == 7:
                    codes[8] = signal
            for signal in signal_patterns:
                if len(signal) == 6:
                    if not codes[1].issubset(signal):
                        codes[6] = signal
                    elif codes[4].issubset(signal):
                        codes[9] = signal
                    else:
                        codes[0] = signal
            for signal in signal_patterns:
                if len(signal) == 5:
                    if codes[1].issubset(signal):
                        codes[3] = signal
                    elif len(codes[4].intersection(signal)) == 3:
                        codes[5] = signal
                    else:
                        codes[2] = signal
            tmp = ''
            for num in output:
                for code in codes:
                    if codes[code] == num:
                        tmp += str(code)
            result += int(tmp)
        print(result)


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-08-input/test-input.txt'
    real_input = 'aoc-08-input/real-input.txt'
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
