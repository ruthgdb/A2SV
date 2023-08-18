class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = set()
        
        def dfs(i):
            left = right = True
            
            if leftChild[i] != -1:
                if leftChild[i] in visited:
                    return False
                
                visited.add(leftChild[i])
                left = dfs(leftChild[i])
                
            if rightChild[i] != -1:
                if rightChild[i] in visited:
                    return False
                
                visited.add(rightChild[i])
                right = dfs(rightChild[i])
                
            return left and right
          
        roots = set(list(range(n)))
        
        for i in range(n):
            if leftChild[i] in roots:
                roots.remove(leftChild[i])
            if rightChild[i] in roots:
                roots.remove(rightChild[i])
            
        if not roots:
            return False
        
        for r in roots:
            root = r
            break
        
        visited.add(root)
        return dfs(root) and len(visited) == n