class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming = [0] * numCourses
        outgoing = defaultdict(set)
        queue = deque()
        count = 0
        
        for course, pre in prerequisites:
            outgoing[pre].add(course)
            incoming[course] += 1
    
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
                
        while queue:
            temp = queue.popleft()
            count += 1
            
            for i in outgoing[temp]:
                incoming[i] -= 1
                if incoming[i]==0:
                    queue.append(i)

        return count == numCourses