class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        full_text = []
        curr_line = []
        word_count = 0
        
        def build_line(line, count, is_last = False):
            if len(line) == 1:
                full_text.append(''.join(line[0] + ' ' * (maxWidth - count)))
                return
            
            remaining_space = maxWidth - count
            text = []
            places = len(line) - 1
            extras = remaining_space % places if not is_last else 0
            spaces = remaining_space // places if not is_last else 1
            
            for i in line:
                if is_last:
                    space = ' ' * 1
                elif extras > 0:
                    space = ' ' * (spaces + 1)
                    extras -= 1
                else:
                    space = ' ' * spaces
                    
                text.append(i)    
                text.append(space)
            
            text.pop()
            
            if is_last and maxWidth - (len(line) - 1 + count) > 0:
                text.append(' ' * (maxWidth - (len(line) - 1 + count)))
             
            full_text.append(''.join(text))
        
        for word in words:
            if len(word) + max(0, len(curr_line)) + word_count <= maxWidth:
                curr_line.append(word)
                word_count += len(word)
            else:
                build_line(curr_line, word_count)
                curr_line = [word]
                word_count = len(word)
                
        build_line(curr_line, word_count, True)
        return full_text