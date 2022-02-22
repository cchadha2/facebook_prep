import heapq

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """O(N^2 * logD) time and O(N) space."""
        
        heap = []
        digit_logs = []
        
        # O(N) time where N is number of logs.
        for log in logs:
            # O(N) time and space for split.
            identifier, contents = log.split(" ", maxsplit=1)
            
            if contents[0].isdigit():
                digit_logs.append(log)
            else:
                # O(logD) time and O(D) space for heap where D is number of letter logs.
                heapq.heappush(heap, (contents, identifier, log))
                
                
        # O(DlogD) time and O(D) space for letter logs.
        letter_logs = []
        while heap:
            letter_logs.append(heapq.heappop(heap)[-1])
            
        # O(N) time and space.
        return letter_logs + digit_logs
        
