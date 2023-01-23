class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * n
        outgoing = [0] * n
        
        for person1, person2 in trust:
            incoming[person2 - 1] += 1
            outgoing[person1 - 1] += 1
            
        for i in range(n):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i + 1
            
        return -1