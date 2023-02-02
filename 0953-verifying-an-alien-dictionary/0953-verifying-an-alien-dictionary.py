class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = defaultdict(str)
        
        for i in range(len(order)):
            alphabet[order[i]] = i
                    
        for i in range(len(words) - 1):
            minLen = min(len(words[i]), len(words[i + 1]))
            for j in range(minLen):
                if alphabet[words[i][j]] > alphabet[words[i + 1][j]]:
                    return False
                elif alphabet[words[i][j]] < alphabet[words[i + 1][j]]: 
                    break

            if words[i][:minLen] == words[i + 1][:minLen] and len(words[i]) != minLen:
                return False

        return True