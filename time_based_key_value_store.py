class TimeMap:

    def __init__(self):
        self.table = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        """O(1) time and space."""
        self.table.setdefault(key, []).append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        """O(log(k)) time and O(1) space where
           k is max length of values under any key k."""
        if not key in self.table:
            return ""
        
        lo, hi = 0, len(self.table[key]) - 1
        ans = None
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if self.table[key][mid][1] > timestamp:
                hi = mid - 1
            elif self.table[key][mid][1] <= timestamp:
                ans = self.table[key][mid][0]
                lo = mid + 1
                
        return ans if ans is not None else ""
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
