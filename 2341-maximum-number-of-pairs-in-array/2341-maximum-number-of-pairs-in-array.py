class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = [0, 0]
        
        for i in c:
            res[0] += c[i] // 2
            if c[i] % 2 != 0:
                res[1] += 1
                
        return res