# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        # O(N) time and O(N) space where N is number of elements in nestedList (int or list).
        max_depth = 1
        # Do one iteration over the nestedList and find the max depth.
        def find_max_depth(arr, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            
            for elem in arr:
                if not elem.isInteger():
                    find_max_depth(elem.getList(), depth + 1)
            
                    
        find_max_depth(nestedList, 1) 
                
        # Go over the nestedList again and recursively calculate each integer or list's value.
        def calculate_value(arr, depth):
            
            value = 0
            for elem in arr:
                if elem.isInteger():
                    value += (max_depth - depth + 1) * (elem.getInteger())
                else:
                    value += calculate_value(elem.getList(), depth + 1)
                    
            return value
                    
            
        return calculate_value(nestedList, 1)
