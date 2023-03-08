class Solution:
    def minEatingSpeed(self, piles: List[int], hour: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            speed = 0

            for pile in piles:
                speed += math.ceil(pile / mid)

            if speed > hour:
                left = mid + 1
            else:
                right = mid
           

        return left