class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """O(N) time and O(N) space where N is length of num string."""
        
        def parse_string(num):
            """O(N) time and O(1) space where N is length of num string."""
            
            real = idx = 0
            real_negative = False
            if num[idx] == "-":
                real_negative = True
                idx += 1
            
            while idx < len(num) and num[idx].isdigit():
                real = (real * 10) + int(num[idx])
                idx += 1
                
            real = real if not real_negative else -real
            
            idx += 1
            complex_negative = False 
            if num[idx] == "-":
                complex_negative = True
                idx += 1
            
            complex_num = 0
            while idx < len(num) and num[idx].isdigit():
                complex_num = (complex_num * 10) + int(num[idx])
                idx += 1
                
            complex_num = complex_num if not complex_negative else -complex_num
                
            return real, complex_num
        
        
        real_num1, complex_num1 = parse_string(num1)
        real_num2, complex_num2 = parse_string(num2)
        
        real_part = complex_part = 0
        
        real_part += (real_num1 * real_num2)
        real_part += -(complex_num1 * complex_num2)
        
        complex_part += (real_num1 * complex_num2)
        complex_part += (real_num2 * complex_num1)
        
        return str(real_part) + "+" + str(complex_part) + "i"
