class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = defaultdict(int)
        prefSum = [0]
        count = 0
        
        for num in nums:
            prefSum.append(prefSum[-1] + num)
                        
        for i in range(len(prefSum)):
            count += mods[prefSum[i] % k]
            mods[prefSum[i] % k] += 1
            
        return count