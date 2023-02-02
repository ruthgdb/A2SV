class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        
        for log in logs:
            temp = log.split(' ')
            if temp[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append((temp[1:], temp[0]))
        
        letterLogs.sort()
        return [' '.join([log[1]] + log[0]) for log in letterLogs] + digitLogs