class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        def calculateTime(gType):
            dist = 0
            t = 0

            for i in range(len(garbage)):
                count = garbage[i].count(gType)

                if i > 0:
                    t += travel[i - 1]

                if count > 0:
                    dist += count + t
                    t = 0
                    
            return dist
        
        return calculateTime('P') + calculateTime('G') + calculateTime('M')