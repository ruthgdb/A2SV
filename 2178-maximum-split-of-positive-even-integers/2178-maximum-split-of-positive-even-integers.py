class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum %2 != 0:
            return []
        
        num = 2
        res = []
        
        while num <= finalSum:
            if num < finalSum - num:
                res.append(num)
                finalSum -= num
                num += 2
            else:
                res.append(finalSum)
                break
            
        return res