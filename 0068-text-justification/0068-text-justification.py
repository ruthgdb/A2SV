class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        full_text = []
        curr_line = []
        word_count = 0
        
        def build_line(line, count):
            remaining_space = maxWidth - count
            text = []
            places = len(line) - 1
            
            if places == 0:
                return ''.join(line[0] + ' ' * remaining_space)
            
            extras = remaining_space % places
            spaces = remaining_space // places
            
            for i in line:
                text.append(i)
                if extras > 0:
                    space = ' ' * (spaces + 1)
                    extras -= 1
                else:
                    space = ' ' * spaces
                text.append(space)
            
            text.pop()
            return ''.join(text)
        
        for word in words:
            if len(word) + max(0, len(curr_line)) + word_count <= maxWidth:
                curr_line.append(word)
                word_count += len(word)
            else:
                text = build_line(curr_line, word_count)
                full_text.append(text)
                curr_line = [word]
                word_count = len(word)
                
        if curr_line:
            text = []
            remaining_space = maxWidth - word_count
            
            for i in curr_line:
                text.append(i)
                
                if remaining_space > 0:
                    text.append(' ')
                    remaining_space -= 1
               
            if remaining_space > 0:
                text.append(' ' * remaining_space)
                
            full_text.append(''.join(text))
        
        return full_text