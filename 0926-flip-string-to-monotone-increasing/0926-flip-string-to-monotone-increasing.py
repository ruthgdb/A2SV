class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroCount = s.count('0')
        flips = zeroCount  
        onesFlipped = 0
        count = 0
        
        for i in s:
            if i == '0':
                zeroCount -= 1
            else:
                onesFlipped += 1
            flips = min(flips, zeroCount + onesFlipped)
            
        return flips