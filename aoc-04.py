def solution_part1(input_file):
    with open(input_file) as file:
        h1 = set()
        h2 = set()
        h3 = set()
        h4 = set()
        h5 = set()
        v1 = set()
        v2 = set()
        v3 = set()
        v4 = set()
        v5 = set()
        block_line_count = 1
        blocks = []
        for counter, line in enumerate(file):
            line = str(line).strip()
            if counter == 0:
                drawn_numbers = list(map(str, str(line).strip().split(',')))
            elif counter == 1:
                continue
            else:
                if line:
                    numbers_input = line.split(' ')
                    numbers = [x for x in numbers_input if x]
                    vertical_line_count = 1
                    for number in numbers:
                        if block_line_count == 1:
                            h1.add(number)
                        elif block_line_count == 2:
                            h2.add(number)
                        elif block_line_count == 3:
                            h3.add(number)
                        elif block_line_count == 4:
                            h4.add(number)
                        elif block_line_count == 5:
                            h5.add(number)
                        if vertical_line_count == 1:
                            v1.add(number)
                        elif vertical_line_count == 2:
                            v2.add(number)
                        elif vertical_line_count == 3:
                            v3.add(number)
                        elif vertical_line_count == 4:
                            v4.add(number)
                        elif vertical_line_count == 5:
                            v5.add(number)
                        vertical_line_count += 1
                    block_line_count += 1
                else:
                    blocks.append([h1, h2, h3, h4, h5, v1, v2, v3, v4, v5])
                    h1 = set()
                    h2 = set()
                    h3 = set()
                    h4 = set()
                    h5 = set()
                    v1 = set()
                    v2 = set()
                    v3 = set()
                    v4 = set()
                    v5 = set()
                    block_line_count = 1
        blocks.append([h1, h2, h3, h4, h5, v1, v2, v3, v4, v5])
        found = False
        for number in drawn_numbers:
            if found:
                break
            for block in blocks:
                for line in block:
                    if number in line:
                        line.remove(number)
                        if not line:
                            result = 0
                            for num in block[0]:
                                result += int(num)
                            for num in block[1]:
                                result += int(num)
                            for num in block[2]:
                                result += int(num)
                            for num in block[3]:
                                result += int(num)
                            for num in block[4]:
                                result += int(num)
                            print(result * int(number))
                            found = True


def solution_part2(input_file):
    with open(input_file) as file:
        h1 = set()
        h2 = set()
        h3 = set()
        h4 = set()
        h5 = set()
        v1 = set()
        v2 = set()
        v3 = set()
        v4 = set()
        v5 = set()
        block_line_count = 1
        blocks = []
        for counter, line in enumerate(file):
            line = str(line).strip()
            if counter == 0:
                drawn_numbers = list(map(str, str(line).strip().split(',')))
            elif counter == 1:
                continue
            else:
                if line:
                    numbers_input = line.split(' ')
                    numbers = [x for x in numbers_input if x]
                    vertical_line_count = 1
                    for number in numbers:
                        if block_line_count == 1:
                            h1.add(number)
                        elif block_line_count == 2:
                            h2.add(number)
                        elif block_line_count == 3:
                            h3.add(number)
                        elif block_line_count == 4:
                            h4.add(number)
                        elif block_line_count == 5:
                            h5.add(number)
                        if vertical_line_count == 1:
                            v1.add(number)
                        elif vertical_line_count == 2:
                            v2.add(number)
                        elif vertical_line_count == 3:
                            v3.add(number)
                        elif vertical_line_count == 4:
                            v4.add(number)
                        elif vertical_line_count == 5:
                            v5.add(number)
                        vertical_line_count += 1
                    block_line_count += 1
                else:
                    blocks.append([h1, h2, h3, h4, h5, v1, v2, v3, v4, v5])
                    h1 = set()
                    h2 = set()
                    h3 = set()
                    h4 = set()
                    h5 = set()
                    v1 = set()
                    v2 = set()
                    v3 = set()
                    v4 = set()
                    v5 = set()
                    block_line_count = 1
        blocks.append([h1, h2, h3, h4, h5, v1, v2, v3, v4, v5])
        found = False
        blocks_ok = {x for x in range(len(blocks))}
        for number in drawn_numbers:
            if found:
                break
            for block_id, block in enumerate(blocks):
                for line in block:
                    if number in line and not found:
                        line.remove(number)
                        if not line:
                            if block_id in blocks_ok:
                                blocks_ok.remove(block_id)
                            if not blocks_ok:
                                result = 0
                                for num in block[0]:
                                    result += int(num)
                                for num in block[1]:
                                    result += int(num)
                                for num in block[2]:
                                    result += int(num)
                                for num in block[3]:
                                    result += int(num)
                                for num in block[4]:
                                    result += int(num)
                                print(result * int(number))
                                found = True


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-04-input/test-input.txt'
    real_input = 'aoc-04-input/real-input.txt'
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
