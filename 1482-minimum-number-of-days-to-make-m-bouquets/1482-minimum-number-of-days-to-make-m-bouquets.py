class Solution:
    def no_of_boquets(self, arr, days, k):
        bouqets = 0
        count = 0

        for flower in arr:
            if count == k:
                bouqets += 1
                count = 0

            if flower <= days:
                count += 1
            else:
                count = 0
            
        if count == k:
            bouqets += 1
            
        return bouqets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minimum = min(bloomDay)
        maximum = max(bloomDay)
        found = False

        while minimum <= maximum:
            mid = (minimum + maximum) // 2
            
            valid_bouqets = self.no_of_boquets(bloomDay, mid, k)
            
            if valid_bouqets < m:
                minimum = mid + 1
            else:
                found = True
                maximum = mid - 1

        return minimum if found else -1