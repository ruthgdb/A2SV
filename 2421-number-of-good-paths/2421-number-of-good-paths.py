class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        links = defaultdict(list)
        for a, b in edges:
            links[a].append(b)
            links[b].append(a)

        by_value = defaultdict(list)
        for n, val in enumerate(vals): by_value[val].append(n)

        if len(by_value) == len(vals):
            return len(vals)
        elif len(by_value) == 1:
            return len(vals)*(len(vals)+1)//2
            
        parent = list(range(len(vals)))

        def ancestor(n):
            while parent[n] != n:
                n, parent[n] = parent[n], parent[parent[n]]
            return n

        def merge(a, b):
            aa, ab = ancestor(a), ancestor(b)
            parent[max(aa, ab)] = min(aa, ab)
        
        paths = 0
        for val, nodes in sorted(by_value.items()):
            
            for n in nodes:
                for nn in links[n]:
                    if vals[nn] <= val:
                        merge(n, nn)
            
            groups = defaultdict(int)
            for n in nodes:
                groups[ancestor(n)]+=1
            
            paths += sum(k*(k+1)//2 for k in groups.values())

        return paths
