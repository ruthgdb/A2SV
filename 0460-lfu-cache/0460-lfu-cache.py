class Node: 
    def __init__(self, key, val, count = 0, prv=None, nxt=None): 
        self.key = key
        self.val = val
        self.count = count
        self.prv = prv
        self.nxt = nxt

class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.dicnodes = {}
        self.diccnts = {}
        self.mincnt = 0
        
    def get(self, key: int) -> int:
        if key in self.dicnodes: 
            node = self.dicnodes[key]
            value = node.val
            count = node.count
            head, tail = self.diccnts[count]
            if head == node == tail: 
                self.diccnts.pop(count)
                if count == self.mincnt: 
                    self.mincnt += 1
            elif head == node: 
                self.diccnts[count][0] = node.nxt
                self.diccnts[count][0].prv = None
                node.nxt = None
            elif tail == node: 
                self.diccnts[count][1] = node.prv
                self.diccnts[count][1].nxt = None
                node.prv = None
            if node.prv is None: 
                if node.nxt is not None: 
                    node.nxt.prv = None
                    node.nxt = None
            else: 
                if node.nxt is None: 
                    node.prv.nxt = None
                    node.prv = None
                else: 
                    node.prv.nxt, node.nxt.prv = node.nxt, node.prv
                    node.nxt = None
                    node.prv = None
            if count + 1 not in self.diccnts: 
                self.diccnts[count + 1] = [node, node]
            else: 
                _, newtail = self.diccnts[count + 1]
                newtail.nxt = node
                node.prv = newtail
                self.diccnts[count + 1][1] = node
            node.count += 1
            return value        
        else: 
            return -1

    def put(self, key: int, value: int) -> None:      
        if key in self.dicnodes: 
            # if the key exists in the dictionary, no removal.
            node = self.dicnodes[key]
            node.val = value
            count = node.count
            head, tail = self.diccnts[count]
            if head == node == tail: 
                self.diccnts.pop(count)
                if count == self.mincnt: 
                    self.mincnt += 1
            elif head == node: 
                self.diccnts[count][0] = node.nxt
                self.diccnts[count][0].prv = None
                node.nxt = None
            elif tail == node: 
                self.diccnts[count][1] = node.prv
                self.diccnts[count][1].nxt = None
                node.prv = None
            if node.prv is None: 
                if node.nxt is not None: 
                    node.nxt.prv = None
                    node.nxt = None
            else: 
                if node.nxt is None: 
                    node.prv.nxt = None
                    node.prv = None
                else: 
                    node.prv.nxt, node.nxt.prv = node.nxt, node.prv
                    node.nxt = None
                    node.prv = None
            if count + 1 not in self.diccnts: 
                self.diccnts[count + 1] = [node, node]
            else: 
                _, newtail = self.diccnts[count + 1]
                newtail.nxt = node
                node.prv = newtail
                self.diccnts[count + 1][1] = node
            node.count += 1
        else: 
            # if new key
            if len(self.dicnodes) < self.c: 
                # if new key will not overpass the capacity
                node = Node(key, value, 0)
                self.dicnodes[key] = node
                if 1 in self.diccnts: 
                    head, tail = self.diccnts[1]
                    tail.nxt = node
                    node.prv = tail
                    node.count += 1
                    self.diccnts[1][1] = node
                else: 
                    self.diccnts[1] = [node, node]
                    node.count += 1
                self.mincnt = 1
            else: 
                # if new key overpasses the capacity, we need to remove a key.
                if not self.mincnt in self.diccnts: 
                    return None
                head, tail = self.diccnts[self.mincnt]
                node_tomove = head
                if head == tail: 
                    self.diccnts.pop(self.mincnt)
                else: 
                    head.nxt.prv = None
                    self.diccnts[self.mincnt][0] = head.nxt
                    head.nxt = None
                self.dicnodes.pop(node_tomove.key)
                node = Node(key, value, 0)
                self.dicnodes[key] = node
                if 1 in self.diccnts: 
                    head, tail = self.diccnts[1]
                    tail.nxt = node
                    node.prv = tail
                    node.count += 1
                    self.diccnts[1][1] = node
                else: 
                    self.diccnts[1] = [node, node]
                    node.count += 1
                self.mincnt = 1
                
                    

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)