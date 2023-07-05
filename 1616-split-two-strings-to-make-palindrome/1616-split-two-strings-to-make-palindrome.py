class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if a == a[::-1] or b == b[::-1]:
            return True
        
        def checkPalindrome(s1, s2):
            left = 0
            right = len(s1) - 1
            is_same = False
            is_first = True
            
            while left <= right:
                if is_same:
                    if is_first:
                        if s1[left] == s1[right]: 
                            left += 1
                            right -= 1
                        else:
                            is_first = False
                    else:
                        if s2[left] == s2[right]: 
                            left += 1
                            right -= 1
                        else:
                            return False
                else:
                    if s1[left] == s2[right]:
                        left += 1
                        right -= 1
                    else:
                        is_same = True

            return True
                
        return checkPalindrome(a, b) or checkPalindrome(b, a)