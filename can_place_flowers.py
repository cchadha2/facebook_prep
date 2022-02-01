class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """O(N) time and O(1) space."""
        if len(flowerbed) == 1:
            return (not flowerbed[0]) >= n
        
        count = 0
        
        if not flowerbed[0] and not flowerbed[1]:
            flowerbed[0] = 1
            count += 1
        if not flowerbed[-1] and not flowerbed[-2]:
            flowerbed[-1] = 1
            count += 1
        
        start, middle, end = 0, 1, 2
        while end < len(flowerbed):
            if not flowerbed[start] and not flowerbed[middle] and not flowerbed[end]:
                flowerbed[middle] = 1
                count += 1
                
                start += 2
                middle += 2
                end += 2
            else:
                start += 1
                middle += 1
                end += 1
                
            
        return count >= n
            
