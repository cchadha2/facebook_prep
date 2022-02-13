import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        n = len(matrix)
        
        # O(N^2 * klogk) time and O(k) space.
        for row in range(n):
            for col in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[row][col])
                else:
                    heapq.heappushpop(heap, -matrix[row][col])
               
        return -heapq.heappop(heap)
                
            
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        n = len(matrix)
        
        # O(min(k, n)) time and space.
        for row in range(min(k, n)):
            heap.append((matrix[row][0], row, 0))
            
        # O(min(k, n)) time and space.
        heapq.heapify(heap)
            
        # O(k*min(n, k)log(min(n, k))) time.
        while k:
            
            # Minimum.
            # O(min(n, k)log(min(n,k))) time.
            elem, row, col = heapq.heappop(heap)
            
            # O(min(n, k)log(min(n,k))) time.
            if col < (n - 1):
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
                
            k -= 1
            
        return elem
            
            
