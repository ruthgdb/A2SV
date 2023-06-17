class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        @cache
        def dfs(i, prev) :
            if i == len(arr1):
                return 0
            
            curr = float("inf")
            j = bisect_right(arr2, prev)
            
            if i == 0 or prev < arr1[i]:
                curr = dfs(i + 1, arr1[i])
            
            if j != len(arr2):
                curr = min(1 + dfs(i + 1, arr2[j]), curr)
                
            return curr
        
        res = dfs(0, -1)
        return res if res != float("inf") else -1
