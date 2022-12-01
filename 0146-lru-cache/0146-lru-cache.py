class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0
        self.ptrs = {}

    def get(self, key: int) -> int:
        if key not in self.ptrs:
            return -1

        self.putToFront(key)
        return self.ptrs[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.ptrs:
            self.ptrs[key][0] = value
            self.putToFront(key)
        else:
            self.length += 1
            if self.tail:
                self.tail.next = Node(key)
                temp = self.tail
                self.tail = self.tail.next
                self.tail.prev = temp
            else:
                self.head = Node(key)
                self.tail = self.head
                
            self.ptrs[key] = [value, self.tail]
          
            if self.length > self.capacity:
                self.removeLRUNode()
                self.length -= 1
                
    def putToFront(self, key):
        val, node = self.ptrs[key]
        if not node.next:
            return
        
        before, after = node.prev, node.next
        node.prev, node.next = None, None
        
        if before:
            before.next = after
        else:
            self.head = after
            
        if after:
            after.prev = before
        else:
            self.tail = before
        
        self.tail.next = Node(key)
        temp = self.tail
        self.tail = self.tail.next
        self.tail.prev = temp
        self.ptrs[key] = [val, self.tail]

    def removeLRUNode(self):
        key = self.head.val
        del self.ptrs[key]
        self.head = self.head.next
        self.head.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)