class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = defaultdict(set)
        res = [0] * k
        
        for user, minute in logs:
            users[user].add(minute)
            
        for user in users:
            res[len(users[user]) - 1] += 1
        
        return res