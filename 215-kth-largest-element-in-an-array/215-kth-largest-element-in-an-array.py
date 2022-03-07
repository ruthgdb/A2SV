class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:
                heappush(heap, nums[i])
            elif heap[0] < nums[i]:
                heapreplace(heap, nums[i])
                
        return heap[0]
                
        