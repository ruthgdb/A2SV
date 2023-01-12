class Solution:
    def robotWithString(self, s: str) -> str:
        suffix_min = [None for _ in range(len(s))]
        suffix_min[-1] = s[-1]
        
        for i in range(len(s) - 2, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])
        
        suffix_min.append(chr(ord('z') + 1))
        
        result = []
        stack = []
        idx = 0
        
        while idx < len(s):
            if stack and stack[-1] <= suffix_min[idx]:
                result.append(stack.pop())
            else:
                stack.append(s[idx])
                idx += 1
        
        stack.reverse()
        result += stack
        return "".join(result)
                
                
            