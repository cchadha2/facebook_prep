class Graph:

    def __init__(self, num_vertices, edges):
        self.graph = [[] for _ in range(num_vertices)]

        for from_vert, to_vert in edges:
            self.graph[from_vert].append(to_vert)
            self.graph[to_vert].append(from_vert)

    def __getitem__(self, key):
        return self.graph[key]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = Graph(n, edges)

        components = 0
        visited = set()

        for vert in range(n):
            if vert in visited:
                continue

            components += 1
            stack = [vert]

            while stack:
                curr_vert = stack.pop()

                if curr_vert in visited:
                    continue

                visited.add(curr_vert)

                for adj_vert in graph[curr_vert]:
                    if adj_vert in visited:
                        continue

                    stack.append(adj_vert)

        return components
        
