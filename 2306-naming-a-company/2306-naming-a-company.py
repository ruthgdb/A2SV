class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        validNames = 0
        count = defaultdict(set)
        
        for word in ideas:
            count[word[0]].add(word[1:])
            
        for char1 in count:
            for char2 in count:
                if char1 == char2:
                    continue
                    
                diff = 0
                
                for word1 in count[char1]:
                    if word1 in count[char2]:
                        diff += 1
                
                validNames += (len(count[char1]) - diff) * (len(count[char2]) - diff)
            
        return validNames