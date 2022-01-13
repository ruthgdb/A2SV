class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}':'{', ')':'(', ']':'['}
        if len(s)%2 != 0:
            return False
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if s[i] in dic.values():
                stack.append(s[i])
            else:
                if len(stack) > 0 and dic[s[i]] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
                    