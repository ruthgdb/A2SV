class Solution:
    def buildStack(self, jumps, ordered, parity):
        if parity:
            ordered.sort(reverse = True)
        else:
            ordered.sort(key = lambda x: (x[0], -x[1]))
            
        stack = []
        
        for i in range(len(ordered)):
            idx = 0 if parity else 1
            
            while stack and stack[-1] < ordered[i][1]:
                stack.pop()
                
            if stack:
                jumps[ordered[i][1]][idx] = stack[-1]
            
            stack.append(ordered[i][1])

    def oddEvenJumps(self, arr: List[int]) -> int:
        count = 0
        jumps = defaultdict(lambda: [-1, -1])
        ordered = [(value, idx) for idx, value in enumerate(arr)]
        self.buildStack(jumps, ordered, True)
        self.buildStack(jumps, ordered, False)

        @cache
        def dp(i, parity):
            if i == len(arr) - 1:
                return True
            
            if parity:
                nextJump = jumps[i][0]
                if nextJump != -1:
                    return dp(nextJump, 0)
                return False
            else:
                nextJump = jumps[i][1]
                if nextJump != -1:
                    return dp(nextJump, 1)
                return False
        
        for i in range(len(arr)):
            if dp(i, 1):
                count += 1
                
        return count