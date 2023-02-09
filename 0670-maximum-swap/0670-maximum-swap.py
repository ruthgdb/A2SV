class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        largest = sorted(num, reverse = True)
        idx = -1
        
        for i in range(len(largest)):
            if largest[i] != num[i]:
                idx = i
                break
                
        if idx == -1:
            return int(''.join(num))
        
        maxx = float("-inf")
        idx2 = -1
        
        for i in range(idx, len(num)):
            if int(num[i]) >= maxx:
                maxx = int(num[i])
                idx2 = i
                        
        num[idx], num[idx2] = num[idx2], num[idx]
        return int(''.join(num))