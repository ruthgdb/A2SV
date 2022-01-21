class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        
        for element in s:
            if element == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(element)
                
        for element in t:
            if element == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(element)
        
        return stack1 == stack2