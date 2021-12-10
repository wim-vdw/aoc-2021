from collections import deque


def solution_part1(input_file):
    with open(input_file) as file:
        result = 0
        valid_open_chars = '([{<'
        for line in file:
            open_chars = deque()
            found_error = False
            for char in line.strip():
                if not found_error:
                    if char in valid_open_chars:
                        open_chars.append(char)
                    else:
                        previous_char = open_chars.pop()
                        if previous_char == '(' and char != ')':
                            found_error = True
                        elif previous_char == '[' and char != ']':
                            found_error = True
                        elif previous_char == '{' and char != '}':
                            found_error = True
                        elif previous_char == '<' and char != '>':
                            found_error = True
                        if found_error:
                            if char == ')':
                                result += 3
                            elif char == ']':
                                result += 57
                            elif char == '}':
                                result += 1197
                            else:
                                result += 25137
        print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        result = []
        valid_open_chars = '([{<'
        for line in file:
            open_chars = deque()
            found_error = False
            for char in line.strip():
                if not found_error:
                    if char in valid_open_chars:
                        open_chars.append(char)
                    else:
                        previous_char = open_chars.pop()
                        if previous_char == '(' and char != ')':
                            found_error = True
                        elif previous_char == '[' and char != ']':
                            found_error = True
                        elif previous_char == '{' and char != '}':
                            found_error = True
                        elif previous_char == '<' and char != '>':
                            found_error = True
            if not found_error:
                tmp_result = 0
                while open_chars:
                    tmp = open_chars.pop()
                    if tmp == '(':
                        tmp_result = tmp_result * 5 + 1
                    elif tmp == '[':
                        tmp_result = tmp_result * 5 + 2
                    elif tmp == '{':
                        tmp_result = tmp_result * 5 + 3
                    else:
                        tmp_result = tmp_result * 5 + 4
                result.append(tmp_result)
        print(sorted(result)[len(result) // 2])


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-10-input/test-input.txt'
    real_input = 'aoc-10-input/real-input.txt'
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
