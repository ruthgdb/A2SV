class Solution:
    def decodeString(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
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
                
        return ''.join(stack)
   