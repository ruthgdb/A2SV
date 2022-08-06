class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = log2(buckets)
        t = ceil(minutesToTest / minutesToDie)

        if t == 1:
            return ceil(n)
        
        return ceil(n / log2(t + 1))