class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(N) time and O(1) space solution.
        
        # Search in range [1, arr[0]).
        for elem in range(1, arr[0]):
            if k == 1:
                return elem
            
            k -= 1
        
        # Search in range (arr[0], arr[1])... for all adjacent pairs up to (arr[-2], arr[-1])
        for start_idx in range(len(arr) - 1):
            for elem in range(arr[start_idx] + 1, arr[start_idx + 1]):
                if k == 1:
                    return elem

                k -= 1
        
        # Search in range (arr[-1], 2000]
        for elem in range(arr[-1] + 1, 2001):
            if k == 1:
                return elem
            
            k -= 1
        
        
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(logN) time and O(1) space solution.
        
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            # If number of missing elements to the left is less than k,
            # look to the right.
            if arr[mid] - 1 - mid < k:
                lo = mid + 1
            # Otherwise, look to the left.
            else:
                hi = mid - 1
                
                
        # At the end of the loop, lo = hi + 1,
        # and the kth missing is in-between arr[hi] and arr[lo].
        # The number of integers missing before arr[hi] is
        # arr[hi] - hi - 1 -->
        # the number to return is
        # arr[hi] + k - (arr[hi] - hi - 1) = k + lo
        return lo + k
