class Graph:

    def __init__(self, num_vertices, edges):
        self.graph = [[] for _ in range(num_vertices)]

        for from_vert, to_vert in edges:
            self.graph[from_vert].append(to_vert)
            self.graph[to_vert].append(from_vert)

    def __getitem__(self, key):
        return self.graph[key]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = [False] * n
        on_stack = visited.copy()
        graph = Graph(n, edges)
        cycle = False

        # O(E + V) time for graph and DFS and O(E + V) space for graph.
        def dfs(vertex, prev=-1):
            nonlocal cycle
            if visited[vertex]:
                return
            elif cycle or on_stack[vertex]:
                return

            visited[vertex] = True
            on_stack[vertex] = True

            for adj_vert in graph[vertex]:
                if on_stack[adj_vert] and prev != adj_vert:
                    cycle = True
                    return

                dfs(adj_vert, vertex)

            on_stack[vertex] = False

        components = 0
        for vertex in range(n):
            if not visited[vertex]:
                components += 1

                if components > 1:
                    return False

                dfs(vertex)

        return not cycle
