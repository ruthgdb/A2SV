class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        graph = defaultdict(set)
        visited = set()
        permutations = 0
        
        def backtrack(num, seen):
            nonlocal permutations
            finished = set()
            
            if len(seen) == len(nums):
                permutations += 1
                
            for i, nei in graph[num]:
                if (i, nei) in seen or nei in finished:
                    continue
                seen.add((i, nei))
                finished.add(nei)
                backtrack(nei, seen)
                seen.remove((i, nei))

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                sqrRoot = sqrt(nums[i] + nums[j])
                if int(sqrRoot) ** 2 == nums[i] + nums[j]:
                    graph[nums[i]].add((j, nums[j]))
                    graph[nums[j]].add((i, nums[i])) 
                            
        for i in range(len(nums)):
            if nums[i] not in visited:
                backtrack(nums[i], {(i, nums[i])}) 
                visited.add(nums[i])
            
        return permutations