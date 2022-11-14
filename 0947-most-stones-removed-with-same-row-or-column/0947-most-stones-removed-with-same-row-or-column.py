class Solution:
    def find(self, stone, parents):
        if parents[stone] == stone:
            return stone
        
        parents[stone] = self.find(parents[stone], parents)
        return parents[stone]
        
    def union(self, first_stone, second_stone, parents):
        first_parent = self.find(first_stone, parents)
        second_parent = self.find(second_stone, parents)
        
        if first_parent != second_parent:        
            parents[second_parent] = first_parent
             
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        x x .
        x . x
        . x x
        
        '''
        parents = {}
        component = 0
        
        stones = [(stone[0], stone[1]) for stone in stones]
        
        for stone in stones:
            parents[stone] = stone
            
        for i, stone1 in enumerate(stones):
            for j, stone2 in enumerate(stones):
                if i != j:
                    if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                        self.union(stone1, stone2, parents)
    
        for parent in parents:
            if parents[parent] == parent:
                component += 1
                
        return len(stones) - component