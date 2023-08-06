class Trie:

    def __init__(self):
        self.children = {}
        self.is_eow = False

    def insert(self, word: str) -> None:
        root = self
        
        for char in word:
            if char not in root.children:
                child = Trie()
                root.children[char] = child
                
            root = root.children[char]
            
        root.is_eow = True

    def search(self, word: str) -> bool:
        root = self
        
        for char in word:
            if char not in root.children:
                return False
            
            root = root.children[char]
            
        return root.is_eow

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