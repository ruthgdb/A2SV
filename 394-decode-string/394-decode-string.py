class Solution:
    def decodeString(self, s: str) -> str:
        stack, i, res = [s[0]], 1, ''

        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp, num = '', ''
                
                while stack[-1] != '[':
                    temp = stack.pop() + temp                  
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num        
                stack.append(temp * int(num))
                
            i += 1
            
        for i in stack:
            res += i
            
        return res
   