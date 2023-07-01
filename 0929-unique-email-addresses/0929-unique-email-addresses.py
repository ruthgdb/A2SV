class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        diff_addresses = set()
        
        for email in emails:
            local_name, domain_name = email.split('@')
            
            temp = []
            
            for char in local_name:
                if char == '+':
                    break
                    
                if char.isalpha():
                    temp.append(char)
                    
            diff_addresses.add(''.join(temp) + '@' + domain_name)
            
        return len(diff_addresses)