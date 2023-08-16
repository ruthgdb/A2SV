class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        left = 0
        
        for right in range(len(nums)):
            while queue and queue[-1] < nums[right]:
                queue.pop()
                    
            queue.append(nums[right])
            
            if right - left + 1 > k:
                if queue[0] == nums[left]:
                    queue.popleft()
                left += 1
            
            if right - left + 1 == k:
                res.append(queue[0])
                
        return res