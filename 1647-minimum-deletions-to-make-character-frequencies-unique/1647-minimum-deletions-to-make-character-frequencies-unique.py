class Solution:
    def minDeletions(self, s: str) -> int:
        min_del = 0
        count = Counter(s)
        freq = list(count.values())
        freq.sort()
        count_set = set()
        
        for i in freq:
            if i not in freq:
                count_set.add(i)
            else:
                temp = i
                
                while temp in count_set and temp > 0:
                    temp -= 1
                    
                count_set.add(temp)
                min_del += i - temp
                
        return min_del