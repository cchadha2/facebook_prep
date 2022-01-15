class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def __getitem__(self, key):
        return self.graph[key]

    def __iter__(self):
        return iter(self.graph)

    def add_edge(self, from_vert, to_vert):
        self.graph.setdefault(from_vert, []).append(to_vert)

    def add_vertex(self, vert):
        self.graph.setdefault(vert, [])



class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # O(M) time and O(1) space for 26 letters.
        # where M is length of word.
        if len(words) == 1:
            return "".join(set(words[0]))

        num_letters = 26
        start = ord("a")
        graph = DirectedGraph()

        # O(M) time and space to add vertices and edges to graph.
        def compare_words(word1, word2):

            end = 0
            first_diff = False
            for idx in range(len(word1)):
                if not first_diff and idx >= len(word2):
                    return False
                elif not first_diff and word1[idx] != word2[idx]:
                    graph.add_edge(word1[idx], word2[idx])
                    first_diff = True

                graph.add_vertex(word1[idx])

            for idx in range(len(word2)):
                graph.add_vertex(word2[idx])

            return True


        # O(WM) time where W is number of words.
        for idx in range(len(words) - 1):
            if not compare_words(words[idx], words[idx + 1]):
                return ""


        visited = [False] * num_letters
        on_stack = visited.copy()
        cycle = False
        post_order = []

        # O(E + V) time but only 26 V at most and each
        # vertex can have at most 25 edges so it is also
        # technically constant time and space.
        def dfs(char):
            nonlocal cycle
            vertex = ord(char) - start
            if cycle or visited[vertex]:
                return
            elif on_stack[vertex]:
                cycle = True
                return

            visited[vertex] = True
            on_stack[vertex] = True

            for adj_char in graph[char]:
                adj_vertex = ord(adj_char) - start
                if on_stack[adj_vertex]:
                    cycle = True
                    return
                if visited[adj_vertex]:
                    continue

                dfs(adj_char)

            post_order.append(char)
            on_stack[vertex] = False


        for char in graph:
            dfs(char)
            if cycle:
                return ""

        # O(1) time and space for max 26 characters.
        return "".join(post_order[::-1])
