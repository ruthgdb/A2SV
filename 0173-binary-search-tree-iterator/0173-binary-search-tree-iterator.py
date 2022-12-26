# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.buildHashMap(root)
        self.idx = 0

    def next(self) -> int:
        if self.idx < len(self.arr):
            self.idx += 1
            return self.arr[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.arr)
        
    def buildHashMap(self, root):        
        if root.left:
            self.buildHashMap(root.left)
        
        self.arr.append(root.val)
        
        if root.right:
            self.buildHashMap(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()