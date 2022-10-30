class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = shifts[::-1]
        pref_sum = [shifts[0] % 26]
        shifted_string = []
        
        for i in range(1, len(shifts)):
            pref_sum.append((pref_sum[-1] + shifts[i]) % 26)
        
        pref_sum = pref_sum[::-1]
        
        for i in range(len(s)):
            letter = ord(s[i]) + pref_sum[i]
            if letter > 122:
                letter = 96 + (letter % 122)
                
            shifted_string.append(chr(letter))
            
        return ''.join(shifted_string)