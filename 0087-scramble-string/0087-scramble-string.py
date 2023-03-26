class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @cache
        def dp(first, second):
            if first == second:
                return True
            
            if len(first) == 1:
                return 
            
            firstFromFront = defaultdict(int)
            secondFromFront = defaultdict(int)
            secondFromBack = defaultdict(int)
            j = len(first) - 1
            
            for i in range(len(first) - 1):
                firstFromFront[first[i]] += 1
                secondFromFront[second[i]] += 1
                secondFromBack[second[j]] += 1
                
                if firstFromFront == secondFromFront:
                    if dp(first[:i + 1], second[:i + 1]) and dp(first[i + 1:], second[i + 1:]):
                        return True
                    
                if firstFromFront == secondFromBack:
                    if dp(first[:i + 1], second[j:]) and dp(first[i + 1:], second[:j]):
                        return True
                   
                j -= 1
                    
            return False
            
        return dp(s1, s2)