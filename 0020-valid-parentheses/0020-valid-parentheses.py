class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { '(': ')', '[': ']', '{': '}' }
        stack = []
        
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if not stack or brackets[stack[-1]] != i:
                    return False
                
                stack.pop()
                
        return len(stack) == 0