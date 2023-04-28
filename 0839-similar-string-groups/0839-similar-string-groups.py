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
        
    def are_similar(self, s1, s2):
        diff = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
             
        if not diff or len(diff) == 2:
            return True
        
        return False
  
    
    def numSimilarGroups(self, strs: List[str]) -> int:
        parents = {}
        groups = 0
        
        for s in strs:
            parents[s] = s
            
        for i, s1 in enumerate(strs):
            for j, s2 in enumerate(strs):
                if i != j and self.are_similar(s1, s2):
                    self.union(s1, s2, parents)
            
        for s in strs:
            self.find(s, parents)
            
        for parent in parents:
            if parents[parent] == parent:
                groups += 1
                
        return groups