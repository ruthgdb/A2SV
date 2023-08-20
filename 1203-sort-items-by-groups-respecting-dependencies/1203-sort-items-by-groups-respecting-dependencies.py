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
            ''' This function builds the dependencies between items in a group
            it returns False if there is a cycle between the items
            '''
            inner_queue = deque()
            visited = set()
            
            # add individual items that are independent
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
        
        # building groups
        for i, item in enumerate(group):
            groups[item].append(i)
            
        # bulding dependecies among items
        for i, deps in enumerate(beforeItems):
            for dep in deps:
                incoming[i] += 1
                graph[dep].append(i)
            
        # building dependencies among groups
        for i, deps in enumerate(beforeItems):
            for dep in deps:
                if group[i] == -1:
                    groupless_deps[i] += 1   
                else:
                    if group[i] != group[dep]:
                        group_incoming[group[i]] += 1

        # adding independent groups to build graph   
        for i, g in enumerate(group_incoming):
            if g == 0:
                queue.append((i, True))
              
        # adding independent groupless items to queue
        for i in groups[-1]:
            if i not in groupless_deps:
                queue.appendleft((i, False)) # because its not a group
             
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