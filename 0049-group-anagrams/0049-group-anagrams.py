class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []
        
        for s in strs:
            groups[tuple(sorted(s))].append(s)
            
        return groups.values()