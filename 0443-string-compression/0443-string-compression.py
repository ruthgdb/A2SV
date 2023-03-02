class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        count = 1
        countPtr = 1
        
        for right in range(1, len(chars)):
            if chars[left] != chars[right]:
                if count > 1:
                    count = str(count)
                    
                    for i in range(len(count)):
                        chars[countPtr] = count[i]
                        countPtr += 1
                        
                chars[countPtr] = chars[right]    
                left = right
                count = 1
                countPtr += 1 
            else:
                count += 1
            
                
        if count > 1:
            count = str(count)

            for i in range(len(count)):
                chars[countPtr] = count[i]
                countPtr += 1
          
        n = len(chars)
        for _ in range(n - countPtr):
            chars.pop()
                
        return len(chars)