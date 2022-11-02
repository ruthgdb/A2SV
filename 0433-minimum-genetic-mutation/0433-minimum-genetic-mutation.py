class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: 
            return -1
        
        bank.append(start)
        visited = set(start)
        queue = deque([start])
        min_len = 0
        mutations = defaultdict(list)
        
        for gene in bank:
            for i in range(8):
                changes = gene[:i] + '*' + gene[i + 1:]
                mutations[changes].append(gene)
                                    
        while queue:
            l = len(queue)
            
            for i in range(l):
                curr_mutation = queue.popleft()
                if curr_mutation == end:
                    return min_len
                
                for i in range(len(curr_mutation)):
                    changes = curr_mutation[:i] + '*' + curr_mutation[i + 1:]
                    
                    for match in mutations[changes]:
                        if match not in visited:
                            queue.append(match)
                            visited.add(match)
            min_len += 1
                            
        return -1