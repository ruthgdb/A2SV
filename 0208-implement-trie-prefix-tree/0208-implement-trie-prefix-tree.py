class Trie:

    def __init__(self):
        self.children = {}
        self.isEOW = False

    def insert(self, word: str) -> None:
        root = self
        
        for char in word:
            if char in root.children:
                root = root.children[char]
            else:
                newNode = Trie()
                root.children[char] = newNode
                root = newNode
                
        root.isEOW = True

    def search(self, word: str) -> bool:
        root = self
        
        for char in word:
            if char not in root.children:
                return False
            
            root = root.children[char]
            
        return root.isEOW

    def startsWith(self, prefix: str) -> bool:
        root = self
        
        for char in prefix:
            if char not in root.children:
                return False
            
            root = root.children[char]
            
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)