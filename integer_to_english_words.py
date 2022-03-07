class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
                 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
                 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        
        
        magnitudes = [" ", " Thousand", " Million", " Billion"]
        
        
        def generate_words(text, order):
            if len(text) < 3:
                text = "0" * (3 - len(text)) + text
                
            if text[1] == "1":
                yield words[int(text[1:])] + order
            else:
                returned = False
                if text[2] != "0":
                    yield words[int(text[2])] + order
                else:
                    if text[1] != "0":
                        returned = True
                        yield words[int(text[1]) * 10] + order
                
                if text[1] != "0" and not returned:
                    yield words[int(text[1]) * 10]
                    
            if text[0] != "0":
                yield words[int(text[0])] + " Hundred"
           
        
        str_num = str(num)
        res = ""
        for order, start in zip(magnitudes, range(len(str_num) - 3, -3, -3)):
            real_start = max(0, start)
            end = real_start + 3
            if start < 0:
                end += start
                
            text = ""
            for word in generate_words(str_num[real_start : end], order):
                text = word + " " +  text
                
            if text and not text.rstrip().endswith(order):
                text = text.rstrip()
                text += order + " "
                
            res = text + res
            
        return res.rstrip()
           
