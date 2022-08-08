class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def bk(total, candidates, path):
            if total == target:
                res.append(path)
                return
                
            if total > target:
                return
            
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                bk(total + candidates[i], candidates[i + 1:], path + [candidates[i]])
            
        bk(0, candidates, [])
        return res