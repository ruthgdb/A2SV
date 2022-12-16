class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        stack = []
        
        for i in pushed:
            stack.append(i)
            
            while stack and stack[-1] == popped[idx]:
                idx += 1
                stack.pop()
        
        return idx == len(popped)