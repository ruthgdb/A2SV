from collections import defaultdict
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        visited = set()
        nodes = defaultdict(list)

        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0]) 
        
        def dfs(node, parent): 
            for nod in nodes[node]:
                if nod in visited and nod != parent:
                    return False

                elif nod not in visited:
                    visited.add(nod)
                    dfs(nod, node)
                    

        visited.add(0)
        result = dfs(0, -1)

        if len(visited) == n and result == None:
            return True
        return False