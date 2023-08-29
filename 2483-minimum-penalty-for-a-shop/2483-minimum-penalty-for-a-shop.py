class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref_sum = [int(customers[0] == 'N')]
        post_sum = [int(customers[-1] == 'Y')]
        
        for i in range(1, len(customers)):
            pref_sum.append(pref_sum[-1] + int(customers[i] == 'N'))
            
        for i in range(len(customers) - 2, -1, -1):
            post_sum.append(post_sum[-1] + int(customers[i] == 'Y'))
          
        post_sum.reverse()
        min_cost = post_sum[0]
        min_hour = 0
        
        for i in range(len(customers)):
            before = pref_sum[i - 1] if i > 0 else 0
            after = post_sum[i]
            
            if before + after < min_cost:
                min_cost = before + after
                min_hour = i
                
        if pref_sum[-1] < min_cost:
            min_hour = len(customers)
            
        return min_hour