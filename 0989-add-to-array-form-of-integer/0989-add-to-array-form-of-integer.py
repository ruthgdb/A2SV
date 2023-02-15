class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(i) for i in num]
        res = list(str(int(''.join(num)) + k))
        return [int(i) for i in res]