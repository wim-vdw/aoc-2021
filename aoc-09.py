def solution_part1(input_file):
    with open(input_file) as file:
        heatmap_input = [line.strip() for line in file]
    heatmap = [[x for x in line] for line in heatmap_input]
    max_y = len(heatmap)
    max_x = len(heatmap[0])
    found = set()
    for y in range(max_y):
        for x in range(max_x):
            if 0 < x < max_x - 1 and 0 < y < max_y - 1:
                if heatmap[y][x] < heatmap[y][x - 1] and heatmap[y][x] < heatmap[y][x + 1] and heatmap[y][x] < \
                        heatmap[y - 1][x] and heatmap[y][x] < heatmap[y + 1][x]:
                    found.add((x, y))
            elif y == 0:
                if x == 0:
                    if heatmap[y][x] < heatmap[y][x + 1] and heatmap[y][x] < heatmap[y + 1][x]:
                        found.add((x, y))
                elif x == max_x - 1:
                    if heatmap[y][x] < heatmap[y][x - 1] and heatmap[y][x] < heatmap[y + 1][x]:
                        found.add((x, y))
                else:
                    if heatmap[y][x] < heatmap[y][x - 1] and heatmap[y][x] < heatmap[y][x + 1] and heatmap[y][x] < \
                            heatmap[y + 1][x]:
                        found.add((x, y))
            elif y == max_y - 1:
                if x == 0:
                    if heatmap[y][x] < heatmap[y][x + 1] and heatmap[y][x] < heatmap[y - 1][x]:
                        found.add((x, y))
                elif x == max_x - 1:
                    if heatmap[y][x] < heatmap[y][x - 1] and heatmap[y][x] < heatmap[y - 1][x]:
                        found.add((x, y))
                else:
                    if heatmap[y][x] < heatmap[y][x - 1] and heatmap[y][x] < heatmap[y][x + 1] and heatmap[y][x] < \
                            heatmap[y - 1][x]:
                        found.add((x, y))
            elif x == 0:
                if y == 0:
                    if heatmap[y][x] < heatmap[y][x + 1] and heatmap[y][x] < heatmap[y + 1][x]:
                        found.add((x, y))
                elif y == max_y - 1:
                    if heatmap[y][x] < heatmap[y - 1][x] and heatmap[y][x] < heatmap[y][x + 1]:
                        found.add((x, y))
                else:
                    if heatmap[y][x] < heatmap[y - 1][x] and heatmap[y][x] < heatmap[y + 1][x] and heatmap[y][x] < \
                            heatmap[y][x + 1]:
                        found.add((x, y))
            elif x == max_x - 1:
                if y == 0:
                    if heatmap[y][x] < heatmap[y][x - 1] and heatmap[y][x] < heatmap[y + 1][x]:
                        found.add((x, y))
                elif y == max_y - 1:
                    if heatmap[y][x] < heatmap[y - 1][x] and heatmap[y][x] < heatmap[y][x - 1]:
                        found.add((x, y))
                else:
                    if heatmap[y][x] < heatmap[y - 1][x] and heatmap[y][x] < heatmap[y + 1][x] and heatmap[y][x] < \
                            heatmap[y][x - 1]:
                        found.add((x, y))
    result = 0
    for x, y in found:
        result += int(heatmap[y][x]) + 1
    print(result)


def solution_part2(input_file):
    with open(input_file) as file:
        pass


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-09-input/test-input.txt'
    real_input = 'aoc-09-input/real-input.txt'
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
