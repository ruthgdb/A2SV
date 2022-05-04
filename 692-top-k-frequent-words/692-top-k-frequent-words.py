class Trie:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        root = Trie()
        count = defaultdict(int)
        result = []
        
        def search(word) -> bool:
            temp = root
            
            for char in word:
                if char in temp.children:
                    temp = temp.children[char]
                else:
                    return False
                
            return temp.isEndOfWord
        
        def insert(word):
            temp = root
            
            for char in word:
                if char in temp.children:
                    temp = temp.children[char]
                else:
                    newNode = Trie()
                    temp.children[char] = newNode
                    temp = newNode
                    
            temp.isEndOfWord = True
        
        for word in words:
            if search(word):
                count[word] += 1
            else:
                insert(word)
                count[word] += 1
                
        for key in count.keys():
            result.append([-1 * count[key], key])
            
        result.sort()
        
        return [val[1] for val in result[:k]]
            
            