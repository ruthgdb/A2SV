class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        res = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        res.sort()
        min_score = sum(res[:k - 1]) + (weights[0] + weights[-1])
        max_score = sum(res[len(res) - k + 1:]) + (weights[0] + weights[-1])
        return max_score - min_score
