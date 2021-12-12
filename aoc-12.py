from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}
        self.number_of_paths = 0
        self.small_caves = []

    def add_edge(self, start, end):
        if start not in self.graph:
            self.graph[start] = deque()
        if end not in self.graph:
            self.graph[end] = deque()
        self.graph[start].append(end)
        self.graph[end].append(start)

    def find_paths_util_solution1(self, u, d, visited, path):
        if not str(u).isupper():
            visited[u] = True
        path.append(u)
        if u == d:
            self.number_of_paths += 1
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.find_paths_util_solution1(i, d, visited, path)
        path.pop()
        visited[u] = False

    def find_paths_util_solution2(self, u, d, visited, path):
        if not str(u).isupper():
            visited[u] = True
        path.append(u)
        if u == d:
            self.number_of_paths += 1
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.find_paths_util_solution2(i, d, visited, path)
        path.pop()
        visited[u] = False

    def find_paths_solution1(self, start, end):
        self.number_of_paths = 0
        visited = {}
        for element in self.graph:
            visited[element] = False
        path = []
        self.find_paths_util_solution1(start, end, visited, path)
        print(self.number_of_paths)

    def find_paths_solution2(self, start, end):
        self.number_of_paths = 0
        for cave in self.graph:
            if str(cave).islower():
                if cave not in ['start', 'end']:
                    self.small_caves.append(cave)
        visited = {}
        for element in self.graph:
            visited[element] = False
        path = []
        self.find_paths_util_solution2(start, end, visited, path)
        print(self.number_of_paths)


def solution_part1(input_file):
    with open(input_file) as file:
        graph = Graph()
        for line in file:
            start, end = line.strip().split('-')
            graph.add_edge(start, end)
        graph.find_paths_solution1('start', 'end')


def solution_part2(input_file):
    with open(input_file) as file:
        graph = Graph()
        for line in file:
            start, end = line.strip().split('-')
            graph.add_edge(start, end)
        graph.find_paths_solution2('start', 'end')


if __name__ == '__main__':
    real_run = True
    test_input = 'aoc-12-input/test-input.txt'
    real_input = 'aoc-12-input/real-input.txt'
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
