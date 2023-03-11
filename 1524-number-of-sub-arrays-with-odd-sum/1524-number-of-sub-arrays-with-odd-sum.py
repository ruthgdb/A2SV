class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefSum = [0]
        mods = defaultdict(int)
        count = 0
        mod = 10 ** 9 + 7
        
        for num in arr:
            prefSum.append(prefSum[-1] + num)
                    
        for i in range(1, len(prefSum)):
            if prefSum[i] % 2 == 0:
                count += mods[1]
            else:
                count += mods[0]
                count += 1
                
            mods[prefSum[i] % 2] += 1
        
        return count % mod