class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n).replace("0b","")
        l = 32 - len(bits)
        bits = bits[::-1]
        bits = bits + ('0' * l)   
        return int(bits, 2)