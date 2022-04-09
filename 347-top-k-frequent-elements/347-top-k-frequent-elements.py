class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap, result = [], [] 
        
        for key, val in count.items():
            heappush(heap, (-val, key))
        
        for i in range(k):
            temp = heappop(heap)
            result.append(temp[1])
            
        return result
            