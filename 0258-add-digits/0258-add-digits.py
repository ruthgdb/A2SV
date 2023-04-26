class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        
        while num >= 10:
            temp = 0
            
            while num >= 10:
                temp += num % 10
                num = num // 10
                
            temp += num
            num = temp
            
        return num