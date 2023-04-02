class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        return [len(potions) - bisect.bisect_left(potions, math.ceil(success/spell)) for i, spell in enumerate(spells)]