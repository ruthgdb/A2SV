import heapq

class Solution:
    def valid_max(self, val, nums, p):
        heap = []
        visited = set()
        count = 0
        incoming = [0] * len(nums)
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] <= val:
                incoming[i] += 1
                incoming[i + 1] += 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] <= val:
                heappush(heap, (min(incoming[i], incoming[i + 1]), i, i + 1))
              
        # print(heap)
        while heap:
            curr_val, i, j = heappop(heap)
            if i in visited or j in visited:
                continue

            visited.add(i)
            visited.add(j)
            count += 1
        # print(len(visited))
        return len(visited) // 2 >= p
            
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = max(nums) - min(nums)
        best = right
        # print(nums)
        # print(self.valid_max(1, nums, p))
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.valid_max(mid, nums, p):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best