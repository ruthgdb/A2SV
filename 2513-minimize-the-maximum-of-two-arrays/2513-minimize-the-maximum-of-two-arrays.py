class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        _lcm = lcm(divisor1, divisor2)
        
        def can_be(n):
            d1 = n // divisor1
            d2 = n// divisor2
            d12 = n // _lcm
            
            a1 = d2 - d12
            a2 = d1 - d12
            rest = n - (d1 + d2 - d12)
            
            return max(uniqueCnt1 - a1, 0) + max(uniqueCnt2 - a2, 0) <= rest
    
        left, right, best = 0, 10 ** 11, None
        
        while left <= right:
            mid = (left + right) // 2
            if can_be(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best
            