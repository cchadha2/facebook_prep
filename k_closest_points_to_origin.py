"""
Example:

input = [[1, 2], [-1, 4], [2, 3]]
k = 2

distances = [sqrt(5), sqrt(17), sqrt(13)]
output = [[1, 2], [2, 3]]

Naive: Sort the list of points with a euclidean distance function as key => O(NlogN) time where N is number of points and O(N) space for sort.
Heap: Maintain a heap of size k with the negative distance and original indices of the points in the input => O(Nlogk) time and O(k) space.
"""
import heapq

from math import sqrt


def k_closest_points(points, k):

    def distance(x, y):
        return sqrt(x**2 + y**2)


    heap = []

    for idx in range(k):
        heapq.heappush(heap, (-distance(points[idx][0], points[idx][1]), idx))

    for idx in range(k, len(points)):
        heapq.heappushpop(heap, (-distance(points[idx][0], points[idx][1]), idx))

    return [points[idx] for _, idx in heap]
