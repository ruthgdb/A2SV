class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            while left < len(fruits) and len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            res = max(res, right - left + 1)

        return res