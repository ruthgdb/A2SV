class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        total = 0
        for i in range(1, n+1):
            if math.ceil(n / i) - (i // 2) <= 0:
                break
            if i % 2 == 1:
                total += int(n % i == 0)
            else:
                total += int((n % i) / i == 0.5)
        return total