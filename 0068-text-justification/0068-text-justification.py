class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        fullText = []
        line = []
        currLen = 0
        
        for word in words:
            if len(line) + len(word) > maxWidth - currLen:
                for i in range(maxWidth - currLen):
                    idx = i % max(len(line) - 1, 1)
                    line[idx] += ' '
                    
                fullText.append("".join(line))
                line = []
                currLen = 0
                
            currLen += len(word)
            line.append(word)
            
        line = " ".join(line)
        line = line + ' ' * (maxWidth - len(line))
        fullText.append("".join(line))
        
        return fullText