class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_count = 0
        y_count = customers.count('Y')
        min_cost = y_count
        min_hour = 0
        
        for i in range(len(customers)):
            if n_count + y_count < min_cost:
                min_cost = n_count + y_count
                min_hour = i
                
            n_count += customers[i] == 'N'
            y_count -= customers[i] == 'Y'
                
        return min_hour if n_count >= min_cost else len(customers)