class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dif = len(a) - len(b)
        
        if dif > 0:
            b = ('0' * dif) + b
        elif dif < 0:
            a = ('0' * -dif) + a

        l = len(a)
        res = ['0'] * (l + 1)
        carry = 0
    
        for i in range(l - 1, -1, -1):
            currA = int(a[i])
            currB = int(b[i])
            temp = currA + currB
            
            if carry == 1:
                temp += 1 
                
            if temp == 2:
                res[i + 1] = '0'
                carry = 1
            elif temp == 3:
                res[i + 1] = '1'
                carry = 1
            else:
                res[i + 1] = str(temp)
                carry = 0
                
        if carry == 1:
            res[0] = '1'
        else:
            res = res[1:]
            
        return ''.join(res)