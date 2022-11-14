class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [(0, -1)]
        longest_valid_substring = 0
        
        for i, char in enumerate(s):
            if char == ')' and stack and stack[-1][0] == '(':
                stack.pop()
            else:
                stack.append((char, i))
                
        stack.append((-1, len(s)))
        
        for i in range(len(stack) - 1):
            longest_valid_substring = max(longest_valid_substring, stack[i + 1][1] - stack[i][1] - 1)
            
        return longest_valid_substring