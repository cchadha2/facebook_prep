# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """O(N) time and O(1) space."""
        
        celeb_candidate = 0
        for person in range(n):
            if person == celeb_candidate:
                continue
                
            if knows(celeb_candidate, person):
                celeb_candidate = person
                
        count = 0
        for person in range(n):
            if person == celeb_candidate:
                continue
                
            if knows(celeb_candidate, person):
                return -1
                
            if knows(person, celeb_candidate):
                count += 1
                
        return celeb_candidate if count == (n - 1) else -1
            
