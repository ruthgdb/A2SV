class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        pairs = 0
        
        for i in range(len(target)):
            num1, num2 = target[:i], target[i:]
            
            if num1 in count and num2 in count:
                if num1 == num2:
                    pairs += (count[num1] * (count[num2] - 1))
                else:
                    if num1 + num2 == target:
                        pairs += count[num1] * count[num2]
        
        return pairs