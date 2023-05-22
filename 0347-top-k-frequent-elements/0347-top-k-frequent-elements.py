class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [(count[i], i) for i in count]
        freq.sort(reverse = True)
        ans = [x[1] for x in freq][:k]
        return ans