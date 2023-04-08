"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        
        clone = Node(node.val)
        nodes = defaultdict(None)
        nodes[node.val] = clone

        q = deque([node])
        
        while q:
            curr = q.popleft()
            cl = nodes[curr.val]
            for ne in curr.neighbors:
                if ne.val not in nodes:
                    new = Node(ne.val)
                    nodes[ne.val] = new
                    q.append(ne)
                cl.neighbors.append(nodes[ne.val])
                  
        return clone