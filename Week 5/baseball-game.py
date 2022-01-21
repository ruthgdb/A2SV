class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for op in ops:
            if op == '+':
                temp = int(stack.pop())
                temp2 = int(stack.pop())
                stack.append(temp2)
                stack.append(temp)
                stack.append(temp + temp2)
            elif op == 'D':
                temp = int(stack.pop())
                stack.append(temp)
                stack.append(temp*2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)