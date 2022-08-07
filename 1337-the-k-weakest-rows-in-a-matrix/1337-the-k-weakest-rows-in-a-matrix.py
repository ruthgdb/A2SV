class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest = [(a.count(1), i) for i, a in enumerate(mat)]
        res = []
        heapq.heapify(weakest)
        
        while len(res) < k:
            temp = heapq.heappop(weakest)
            res.append(temp[1])
        
        return res