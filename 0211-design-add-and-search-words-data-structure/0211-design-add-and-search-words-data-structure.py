class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEOW = False

    def addWord(self, word: str) -> None:
        root = self
        
        for char in word:
            if char in root.children:
                root = root.children[char]
            else:
                newNode = WordDictionary()
                root.children[char] = newNode
                root = newNode
        
        root.isEOW = True
        
    def search(self, word: str) -> bool:  
        res = [(self, 0)]
        
        while res:
            root, idx = res.pop()
            found = True
            
            for i in range(idx, len(word)):
                if word[i] != '.':
                    if word[i] not in root.children:
                        found = False
                        break

                    root = root.children[word[i]]
                else:
                    for c in root.children:
                        res.append((root.children[c], i + 1))
                        
                    found = False
                    break
                    
            if found and root.isEOW:
                return True
            
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)