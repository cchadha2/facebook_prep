class DirectedGraph:

    def __init__(self, num_vertices, edges):

        self.graph = [[] for _ in range(num_vertices)]

        for from_vert, to_vert in edges:
            self.graph[from_vert].append(to_vert)

    def __getitem__(self, key):
        return self.graph[key]

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        visited = [False] * numCourses
        on_stack = visited.copy()
        cycle = False

        graph = DirectedGraph(numCourses, prerequisites)

        def dfs(vertex):
            nonlocal cycle
            if on_stack[vertex]:
                cycle = True
                return
            if visited[vertex]:
                return

            visited[vertex] = True
            on_stack[vertex] = True

            for adj_vert in graph[vertex]:
                if cycle:
                    return
                elif on_stack[adj_vert]:
                    cycle = True
                    return
                elif visited[adj_vert]:
                    continue

                dfs(adj_vert)

            on_stack[vertex] = False


        for course in range(numCourses):
            dfs(course)
            if cycle:
                return False

        return True


        
