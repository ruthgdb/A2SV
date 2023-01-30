class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        for i in count1:
            for j in count2:  
                l2 = len(count2)
                l1 = len(count1)
                if i != j:
                    if j not in count1:
                        l1 += 1

                    if count2[j] == 1:
                        l2 -= 1

                    if count1[i] == 1:
                        l1 -= 1

                    if i not in count2:
                        l2 += 1
                        
                if l1 == l2:
                    return True

        return False