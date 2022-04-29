class Trie:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def insert(self, word: str) -> None:
        curr = self
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                newNode = Trie()
                curr.children[char] = newNode
                curr = newNode
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self
        
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)