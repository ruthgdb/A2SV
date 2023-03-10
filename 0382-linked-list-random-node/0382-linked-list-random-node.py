# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.indices = {}
        self.i = 0
        
        while head:
            self.indices[self.i] = head.val
            self.i += 1
            head = head.next

    def getRandom(self) -> int:
        r = random.randint(0, self.i - 1)
        return self.indices[r]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()