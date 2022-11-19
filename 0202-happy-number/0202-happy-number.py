class Solution:
    def isHappy(self, n: int) -> bool:
        curr_num = n
        visited = set()
        
        while curr_num not in visited and curr_num > 0:
            visited.add(curr_num)
            curr_num = str(curr_num)
            total = 0
            
            for i in curr_num:
                total += int(i) ** 2
                
            curr_num = total
                      
        return curr_num == 1