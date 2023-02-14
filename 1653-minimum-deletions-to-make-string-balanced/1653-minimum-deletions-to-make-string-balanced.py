class Solution:
    def minimumDeletions(self, s: str) -> int:
        aCount = s.count("a")
        minDel = aCount
        bCount = 0

        for i in s:
            bCount += i == 'b'
            aCount -= i == 'a'
            minDel = min(minDel, bCount + aCount)
            
        return minDel