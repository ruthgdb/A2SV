class Solution:
    def find(self, node, parents):
        if node == parents[node]:
            return node
        
        parents[node] = self.find(parents[node], parents)
        return parents[node]
    
    def union(self, node1, node2, parents):
        parent1 = self.find(node1, parents)
        parent2 = self.find(node2, parents)
        
        if parent1 == parent2:
            return 1
        
        parents[parent1] = parent2
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parents = {}
        extra = 0
        
        for i in range(n):
            parents[i] = i
        
        for node1, node2 in connections:
            if self.union(node1, node2, parents):
                extra += 1
            
        for i in range(n):
            self.find(i, parents)
           
        components = 0
        for parent in parents:
            if parents[parent] == parent:
                components += 1
                
        return components - 1 if components <= extra + 1 else -1