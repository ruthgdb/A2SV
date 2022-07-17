class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set()
        vertices = []
        
        for edge in edges:
            reachable.add(edge[1])
            
        for i in range(n):
            if i not in reachable:
                vertices.append(i)
                
        return vertices