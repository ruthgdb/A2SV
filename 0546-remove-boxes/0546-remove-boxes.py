class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache        
        def dp(left, right, cost):
            if left > right: 
                return 0
            
            while left < right and boxes[left] == boxes[left + 1]:
                left += 1
                cost += 1
                
            maxCost = (cost + 1) ** 2 + dp(left + 1, right, 0)  
            
            for i in range(left + 1, right + 1):  
                if boxes[left] == boxes[i]:
                    betweenBoxes = dp(left + 1, i - 1, 0)
                    afterLastBox = dp(i, right, cost + 1)
                    maxCost = max(maxCost, betweenBoxes + afterLastBox)
               
            return maxCost

        return dp(0, len(boxes) - 1, 0)