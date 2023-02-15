class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        graph = defaultdict(set)
        visited = set()
        visited2 = set()
        permutations = 0
        
        def backtrack(node, visited):
            nonlocal permutations
            finished = set()
            
            if len(visited) == len(nums):
                permutations += 1
                
            for i, nei in graph[node]:
                if (i, nei) not in visited and nei not in finished:
                    visited.add((i, nei))
                    finished.add(nei)
                    backtrack(nei, visited)
                    visited.remove((i, nei))
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                sqrRoot = sqrt(nums[i] + nums[j])
                if int(sqrRoot) ** 2 == nums[i] + nums[j]:
                    graph[nums[i]].add((j, nums[j]))
                    graph[nums[j]].add((i, nums[i])) 
                            
        for i in range(len(nums)):
            if nums[i] not in visited2:
                backtrack(nums[i], {(i, nums[i])}) 
                visited2.add(nums[i])
            
        return permutations