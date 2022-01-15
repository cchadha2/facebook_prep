import heapq

class Heap:

    def __init__(self):
        self.heap = []
        self.deleted = set()

    def add(self, val):
        heapq.heappush(self.heap, val)

    def remove(self, val):
        self.deleted.add(val)

    def print_min(self):
        while True:
            if not self.heap[0] in self.deleted:
                break

            heapq.heappop(self.heap)

        print(self.heap[0])


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    q = int(input().strip())

    heap = Heap()

    for q_itr in range(q):
        query = input().rstrip().split()

        q_type = query[0]

        if q_type == "1":
            heap.add(int(query[1]))
        elif q_type == "2":
            heap.remove(int(query[1]))
        else:
            heap.print_min()
