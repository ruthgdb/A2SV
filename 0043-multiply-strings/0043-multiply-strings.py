class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prod = [0] * (len(num1) + len(num2) + 1)
        res = []
        carry = 0
        
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            
            for j in range(len(num2) - 1, -1, -1):
                mul = int(int(num1[i]) * int(num2[j])) + carry
                prod[i + j + 2] += mul % 10
                carry = mul // 10
              
            if carry > 0:
                prod[i + 1] += carry
                
        prod.reverse()
        carry = 0
        
        for num in prod:
            num = num + carry
            if num < 10:
                res.append(str(num))
                carry = 0
            else:
                res.append(str(num % 10))
                carry = num // 10
                
        res.reverse()
        return str(int(''.join(res)))