class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        result = []
        dec = [0] * len(security)
        inc = [0] * len(security)
        
        for i in range(len(security) - 1):
            if security[i] >= security[i + 1]:
                dec[i + 1] += dec[i] + 1
                
        for i in range(len(security) - 1, 0, -1):
            if security[i] >= security[i - 1]:
                inc[i - 1] += inc[i] + 1
                
        for i in range(time, len(security) - time):
            if dec[i] >= time and inc[i] >= time:
                result.append(i)
                
        return result