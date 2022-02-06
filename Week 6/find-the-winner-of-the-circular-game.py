class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        index = 0
        count = 1
        
        while len(friends) > 1:
            if count == k:
                friends.pop(index)
                count = 1
            else:
                count += 1
                index += 1
                index %= len(friends)
            
        return friends[0]