class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(-score[i], i) for i in range(len(score))]
        heapq.heapify(score)
        res = [''] * len(score)
        count = 1
        
        while score:
            temp = heapq.heappop(score)
            if count == 1:
                res[temp[1]] = "Gold Medal"
            elif count == 2:
                res[temp[1]] = "Silver Medal"
            elif count == 3:
                res[temp[1]] = "Bronze Medal"
            else:
                res[temp[1]] = str(count)
            count += 1
                
        return res