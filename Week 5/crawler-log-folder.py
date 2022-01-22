class Solution:
    def minOperations(self, logs: List[str]) -> int:
        directory = []
        
        for op in logs:
            if op == "../":
                if directory:
                    directory.pop()
            elif op != "./":
                directory.append(op)
                
        return len(directory)