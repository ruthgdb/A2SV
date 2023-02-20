class Solution:
    def checkString(self, s):
        upperAlph = [chr(i) for i in range(97, 97 + 6)]
        lowerAlph = [chr(i) for i in range(65, 65 + 6)]
        
        for i in s:
            if i.isdigit() or i in lowerAlph or i in upperAlph:
                continue
            return False
        
        return True
        
    def checkIPv4(self, IP):
        arr = IP.split('.')
        
        if len(arr) != 4:
            return False
        
        for i in range(4):
            if not arr[i].isdigit() or int(arr[i]) >= 256:
                return False
            
            if arr[i][0] == '0' and len(arr[i]) > 1:
                return False
            
        return True
    
    def checkIPv6(self, IP):
        arr = IP.split(':')
        
        if len(arr) != 8:
            return False
        
        for i in range(8):
            if not arr[i] or len(arr[i]) > 4 or not self.checkString(arr[i]):
                return False
        
        return True
    
    def validIPAddress(self, queryIP: str) -> str:
        if self.checkIPv4(queryIP):
            return "IPv4"
        
        if self.checkIPv6(queryIP):
            return "IPv6"
        
        return "Neither"