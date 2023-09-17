class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        masks = [1 << i for i in range(n)]
        all_visited = (1 << n) - 1
        queue = deque([(i, masks[i]) for i in range(n)])
        steps = 0
        visited_states = [{masks[i]} for i in range(n)]

        while queue:
            count = len(queue)

            while count:
                currentNode, visited = queue.popleft()
                if visited == all_visited:
                    return steps

                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    if new_visited == all_visited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        
        return inf