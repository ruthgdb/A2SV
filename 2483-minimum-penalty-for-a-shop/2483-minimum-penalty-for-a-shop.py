class Solution:
    def bestClosingTime(self, customers: str) -> int:
        post_sum = [int(customers[-1] == 'Y')]
        
        for i in range(len(customers) - 2, -1, -1):
            post_sum.append(post_sum[-1] + int(customers[i] == 'Y'))
          
        post_sum.reverse()
        n_count = 0
        min_cost = post_sum[0]
        min_hour = 0
        
        for i in range(len(customers)):
            if n_count + post_sum[i] < min_cost:
                min_cost = n_count + post_sum[i]
                min_hour = i
                
            n_count += customers[i] == 'N'
                
        return min_hour if n_count >= min_cost else len(customers)