class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        curr1 = curr2 = p1 = p2 = 0
        num1, count1 = encoded1[p1]
        num2, count2 = encoded2[p2]
        
        products = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            
            num_to_add = min(count1 - curr1, count2 - curr2)
            product = num1 * num2
            
            if not products or products[-1][0] != product:
                products.append([num1 * num2, num_to_add])
            else:
                products[-1][1] += num_to_add
                
            curr1 += num_to_add
            curr2 += num_to_add
                
            if curr1 == count1:
                p1 += 1
                curr1 = 0
                
                if p1 < len(encoded1):
                    num1, count1 = encoded1[p1]
                    
            if curr2 == count2:
                p2 += 1
                curr2 = 0
                
                if p2 < len(encoded2):
                    num2, count2 = encoded2[p2]
            
        return products
        
            
        
