class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start).replace("0b","")
        g = bin(goal).replace("0b","")
        dif = len(s) - len(g)
        count = 0
        
        if dif > 0:
            g = ('0' * dif) + g
        elif dif < 0:
            s = ('0' * -dif) + s

        for i in range(len(s)):
            if s[i] != g[i]:
                count += 1
                
        return count