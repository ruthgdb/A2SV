class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        count = 0
        curr = self.head
        
        while curr:
            if count == index:
                return curr.val
            
            count += 1
            curr = curr.next
        
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            newHead = ListNode(val)
            temp = self.head
            self.head = newHead
            newHead.next = temp
        
    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.tail = ListNode(val)
            self.head = self.tail
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
            
        curr = self.head    
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print(444)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
            
        count = 0
        curr = self.head
        
        while curr:
            if count  == index - 1:
                break
            
            count += 1
            curr = curr.next
         
        if curr and not curr.next:
            curr.next = ListNode(val)
            self.tail = curr.next
        elif curr:
            nextt = curr.next
            curr.next = ListNode(val)
            curr = curr.next
            curr.next = nextt
            
        # curr = self.head
        
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print(444)
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
            
        prev = None
        curr = self.head
        count = 0
        
        while curr:
            if count == index:
                break
                
            prev = curr
            count += 1
            curr = curr.next
        
        if not prev:
            if curr.next:
                curr.next = curr.next.next
        elif curr and not curr.next:
            self.tail = prev
            self.tail.next = None
        elif curr:
            prev.next = prev.next.next
            
        curr = self.head    
        # while curr:
        #     print(curr.val)
        #     curr = curr.next
        # print(444)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)