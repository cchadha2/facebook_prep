"""

        0 <--- 1

        ^      ^
        |      |
        |      |

        2 <--- 3

output = [0, 2, 1, 3]
"""
class DiGraph:

    def __init__(self, num_vertices, edges):

        self.graph = [[] for _ in range(num_vertices)]

        for from_vert, to_vert in edges:
            self.graph[from_vert].append(to_vert)

    def __getitem__(self, key):
        return self.graph[key]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        on_stack = [False] * numCourses
        visited = on_stack.copy()
        post_order = []
        cycle = False

        graph = DiGraph(numCourses, prerequisites)

        def dfs(vertex):
            nonlocal cycle
            if cycle or visited[vertex]:
                return
            if on_stack[vertex]:
                cycle = True
                return

            visited[vertex] = True
            on_stack[vertex] = True

            for adj_vert in graph[vertex]:
                if on_stack[adj_vert]:
                    cycle = True
                    return
                elif cycle or visited[adj_vert]:
                    continue

                dfs(adj_vert)

            on_stack[vertex] = False
            post_order.append(vertex)

        for vert in range(numCourses):
            dfs(vert)
            if cycle:
                return []

        return post_order



            
