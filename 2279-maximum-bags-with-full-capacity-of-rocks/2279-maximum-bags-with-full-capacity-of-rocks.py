class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainingCapacity = [capacity[i] - rocks[i] for i in range(len(rocks))]
        remainingCapacity.sort()
        fullBags = 0
        
        for i in range(len(remainingCapacity)):
            if remainingCapacity[i] <= additionalRocks:
                additionalRocks -= remainingCapacity[i]
                remainingCapacity[i] = 0
                fullBags += 1
                
        return fullBags