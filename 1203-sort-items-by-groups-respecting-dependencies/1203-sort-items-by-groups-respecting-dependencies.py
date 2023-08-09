class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        graph = defaultdict(list)
        incoming = [0] * n
        group_incoming = [0] * m
        groupless_deps = defaultdict(int) # item, incoming
        queue = deque()
        res = []
        
        def build_group(g_num):
            inner_queue = deque()
            visited = set()
            
            for i in groups[g_num]:
                if incoming[i] == 0:
                    inner_queue.append(i)
                
            while inner_queue:
                curr_num = inner_queue.popleft()
                res.append(curr_num)
                visited.add(curr_num)
                
                for nxt_num in graph[curr_num]:
                    incoming[nxt_num] -= 1
                    if group[curr_num] != group[nxt_num]:
                        if group[nxt_num] == -1:
                            groupless_deps[nxt_num] -= 1
                            if groupless_deps[nxt_num] == 0:
                                queue.append((nxt_num, False))
                        else:
                            group_incoming[group[nxt_num]] -= 1
                            if group_incoming[group[nxt_num]] == 0:
                                queue.append((group[nxt_num], True))
                            
                    if incoming[nxt_num] == 0 and group[nxt_num] == group[curr_num]:
                        inner_queue.append(nxt_num)
                
            return len(visited) == len(groups[g_num])
        
        for i, item in enumerate(group):
            groups[item].append(i)
            
        for i, deps in enumerate(beforeItems):
            for dep in deps:
                incoming[i] += 1
                graph[dep].append(i)
                
        for i, deps in enumerate(beforeItems):
            for dep in deps:
                if group[i] == -1:
                    groupless_deps[i] += 1   
                else:
                    if group[i] != group[dep]:
                        group_incoming[group[i]] += 1

            
        for i, g in enumerate(group_incoming):
            if g == 0:
                queue.append((i, True))
                
        for i in groups[-1]:
            if i not in groupless_deps:
                queue.appendleft((i, False))
             
        while queue:
            curr_group, is_group = queue.popleft()
            
            if is_group:
                if not build_group(curr_group):
                    return []
            else:
                res.append(curr_group)
                for nxt_num in graph[curr_group]:
                    incoming[nxt_num] -= 1
                    if group[nxt_num] == -1:
                        groupless_deps[nxt_num] -= 1
                        if groupless_deps[nxt_num] == 0:
                            queue.append((nxt_num, False))
                    else:
                        group_incoming[group[nxt_num]] -= 1
                        if group_incoming[group[nxt_num]] == 0:
                            queue.append((group[nxt_num], True))
                            
        return res if len(res) == n else []