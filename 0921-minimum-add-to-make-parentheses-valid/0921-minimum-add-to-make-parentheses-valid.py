class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        needed = 0
        
        for i in s:
            if i == "(":
                stack.append(i)
            elif stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                
        return len(stack)