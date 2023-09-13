class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        right = [0] * n
        res = [1] * n
        
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1
                
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                right[i] = right[i + 1] + 1
                
        for i in range(n):
            res[i] += max(left[i], right[i])
            
        return sum(res)