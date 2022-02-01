# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.gen = self._gen_vals(nestedList)
        self.res = None
    
    def next(self) -> int:
        return self.res
    
    def hasNext(self) -> bool:
        try:
            self.res = next(self.gen)
            return True
        except StopIteration:
            return False
        
    def _gen_vals(self, arr):
        for elem in arr:
            if elem.isInteger():
                yield elem.getInteger()
            else:
                yield from self._gen_vals(elem.getList())
            
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
