class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        
        def backtrack(i, path):
            if i == len(s):
                if len(path) == 4:
                    ips.append('.'.join(path))
                return
            
            if int(path[-1]) != 0 and int(path[-1] + s[i]) < 256:
                path[-1] += s[i]
                backtrack(i + 1, path)
                path[-1] = path[-1][:-1]
            
            path.append(s[i])
            backtrack(i + 1, path)
            path.pop()
        
        backtrack(1, [s[0]])
        return ips