class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = [gas[0] - cost[0]]
        
        for i in range(1, len(gas)):
            res.append(gas[i] - cost[i])
        
        if sum(res) < 0: return -1
        
        gasLeft, idx = 0, -1
        
        for i in range(len(res)):
            gasLeft += res[i]
            if gasLeft < 0:
                idx = i
                gasLeft = 0
                
        return idx + 1