class Solution:
    def find(self, node, parents):
        if node == parents[node]:
            return node

        parents[node] = self.find(parents[node], parents)
        return parents[node]

    def union(self, nei, node, parents, rank):
        p1 = self.find(nei, parents)
        p2 = self.find(node, parents)

        if p1 != p2:
            rank1, count1 = rank[p1]
            rank2, count2 = rank[p2]
            parents[p2] = p1
            
            if rank1 == rank2:
                rank[p1] = (max(rank1, rank2), count1 + count2)
                return max(count1, count2)

            if rank1 > rank2:
                rank[p1] = (rank1, count1)
            else:
                rank[p1] = (rank2, count2)

        return 0
    
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        idx_val_pair = []
        graph = defaultdict(list)
        unique_paths = len(vals)
        parents = {}
        rank = {}
        
        for i in range(len(vals)):
            idx_val_pair.append((vals[i], i))
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        idx_val_pair.sort()
        
        for val, idx in idx_val_pair:
            parents[idx] = idx
            rank[idx] = (val, 1)

            for nei in graph[idx]:
                if vals[nei] <= val and nei in parents:
                    curr_count = self.union(nei, idx, parents, rank)
                    unique_paths += curr_count

        return unique_paths