class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for i in s:
            if i == ')':
                temp = 0
                
                while stack[-1][0] != '(':
                    char, count = stack.pop()
                    temp += count
                    
                char, count = stack.pop()
                
                if temp != 0:
                    stack.append(['*', (temp * 2)])
                else:
                    stack.append(['*', (temp) + count])
            
            else:
                stack.append(["(", 1])
        
        for char, count in stack:
            score += count
            
        return score