class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def bk(path, opens, close):
            if len(path) / 2 == n:
                res.append(''.join(path))
            
            if opens < n:
                bk(path + ['('], opens + 1, close)
                
            if close < opens:
                bk(path + [')'], opens, close + 1)
                
        bk([], 0, 0)
        return res