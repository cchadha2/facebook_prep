class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        upside_down = [None] * 10
        start = ord("0")
        
        upside_down[ord("6") - start] = "9"
        upside_down[ord("9") - start] = "6"
        upside_down[ord("8") - start] = "8"
        upside_down[ord("0") - start] = "0"
        upside_down[ord("1") - start] = "1"
        
        
        path = []
        for digit in num:
            idx = ord(digit) - start
            if upside_down[idx]:
                path.append(upside_down[idx])
            else:
                return False
                
        return "".join(reversed(path)) == num
