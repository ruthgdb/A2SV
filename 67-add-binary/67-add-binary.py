class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = int(a, 2) + int(b, 2)
        return bin(total).replace("0b", "")