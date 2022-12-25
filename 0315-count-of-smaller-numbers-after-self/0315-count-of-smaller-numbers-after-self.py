from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = SortedList()
        ans = []
        
        for num in reversed(nums):
            arr.add(num)
            i = bisect.bisect_left(arr, num)
            ans.append(i)
            
        return ans[::-1]