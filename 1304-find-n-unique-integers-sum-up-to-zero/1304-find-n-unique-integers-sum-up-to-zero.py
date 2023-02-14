class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        
        for i in range(n // 2):
            res.append(i + 1)
            res.append(-(i + 1))
            
        if n % 2 != 0:
            res.append(0)
            
        return res