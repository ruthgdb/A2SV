class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            bits = bin(n).replace("0b","")
            if bits[0] == '1':
                bits = bits[1:]
                
                for bit in bits:
                    if bit != '0':
                        return False
                    
                return True