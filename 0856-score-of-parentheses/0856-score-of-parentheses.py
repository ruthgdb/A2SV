class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for i in s:
            if i == ')':
                char, count = stack.pop()
                
                if stack:
                    stack[-1][1] = stack[-1][1] + 1 if not count else stack[-1][1] + (count * 2)
                else:
                    score = score + 1 if not count else score + (count * 2)
            else:
                stack.append(["(", 0])
                
        return score