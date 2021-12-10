from collections import deque


def find_low_points(heatmap):
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
    return found


def read_input(input_file):
    with open(input_file) as file:
        heatmap_input = [line.strip() for line in file]
    heatmap = [[int(x) for x in line] for line in heatmap_input]
    return heatmap


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {x: deque() for x in range(vertices)}

    def add_edge(self, source, target):
        self.graph[source].append(target)

    def bfs(self, source):
        count = 1
        visited = [False] * self.vertices
        queue = deque()
        queue.append(source)
        visited[source] = True
        while queue:
            s = queue.popleft()
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    count += 1
        return count


def check_heatmap(heatmap, source_x, source_y, target_x, target_y):
    if source_x < 0 or source_x == len(heatmap[0]):
        return False
    if source_y < 0 or source_y == len(heatmap):
        return False
    if target_x < 0 or target_x == len(heatmap[0]):
        return False
    if target_y < 0 or target_y == len(heatmap):
        return False
    return heatmap[source_y][source_x] < heatmap[target_y][target_x] != 9


def solution_part1(input_file):
    heatmap = read_input(input_file)
    found_low_points = find_low_points(heatmap)
    result = 0
    for x, y in found_low_points:
        result += int(heatmap[y][x]) + 1
    print(result)


def solution_part2(input_file):
    heatmap = read_input(input_file)
    found_low_points = find_low_points(heatmap)
    graph = Graph(len(heatmap) * len(heatmap[0]))
    for y in range(len(heatmap)):
        for x in range(len(heatmap[0])):
            graph_index_source = x + len(heatmap[0] * y)
            if check_heatmap(heatmap, x, y, x, y + 1):
                graph_index_target = x + len(heatmap[0] * (y + 1))
                graph.add_edge(graph_index_source, graph_index_target)
            if check_heatmap(heatmap, x, y, x, y - 1):
                graph_index_target = x + len(heatmap[0] * (y - 1))
                graph.add_edge(graph_index_source, graph_index_target)
            if check_heatmap(heatmap, x, y, x + 1, y):
                graph_index_target = x + 1 + len(heatmap[0] * y)
                graph.add_edge(graph_index_source, graph_index_target)
            if check_heatmap(heatmap, x, y, x - 1, y):
                graph_index_target = x - 1 + len(heatmap[0] * y)
                graph.add_edge(graph_index_source, graph_index_target)
    result = []
    for x, y in found_low_points:
        graph_index = x + len(heatmap[0] * y)
        result.append(graph.bfs(graph_index))
    print(sorted(result)[::-1][0] * sorted(result)[::-1][1] * sorted(result)[::-1][2])


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
