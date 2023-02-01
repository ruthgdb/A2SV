class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wCount = 0
        bCount = 0
        l = 0
        minFlips = k
        
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                wCount += 1
            else:
                bCount += 1
                
            if r - l + 1 > k:
                if blocks[l] == 'W':
                    wCount -= 1
                else:
                    bCount -= 1
                l += 1
            if r - l + 1 == k:
                minFlips = min(minFlips, wCount)
                
        return minFlips