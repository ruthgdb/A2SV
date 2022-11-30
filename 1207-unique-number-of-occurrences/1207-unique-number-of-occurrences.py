class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr)
        return len(set(occurences.values())) == len(occurences.values())