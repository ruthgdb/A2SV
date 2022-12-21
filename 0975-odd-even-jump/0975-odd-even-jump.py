class Solution:
    def buildStack(self, arr, jumps):
        ordered = [(value, idx) for idx, value in enumerate(arr)]
        ordered.sort()
        stack = []
        # print(ordered)

        #for odd
        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] < ordered[i][1]:
                stack.pop()
                
            if stack:
                jumps[ordered[i][1]][0] = stack[-1]
            
            stack.append(ordered[i][1])

        stack = []
        ordered.sort(key = lambda x: (x[0], -x[1]))
        
        #for even
        for i in range(len(arr)):
            while stack and stack[-1] < ordered[i][1]:
                stack.pop()
                
            if stack:
                jumps[ordered[i][1]][1] = stack[-1]
            
            stack.append(ordered[i][1])
        
    def oddEvenJumps(self, arr: List[int]) -> int:
        count = 0
        # odd, even
        jumps = defaultdict(lambda: [-1, -1])
        self.buildStack(arr, jumps)

        def dp(i, parity):
            if i == len(arr) - 1:
                return True
            
            # print(i, parity)
            if parity:
                nextJump = jumps[i][0]
                if nextJump != -1:
                    return dp(nextJump, 0)
                else:
                    return False
            else:
                nextJump = jumps[i][1]
                if nextJump != -1:
                    return dp(nextJump, 1)
                else:
                    return False
        
        for i in range(len(arr)):
            if dp(i, 1):
                # print(i)
                count += 1
                
        return count