class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        queue = deque()
        taken_courses = set()
        
        for course1, course2 in prerequisites:
            indegrees[course1] += 1
            graph[course2].append(course1)
            
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
                
        while queue:
            curr_course = queue.popleft()
            
            if curr_course in taken_courses:
                continue
                
            taken_courses.add(curr_course)
            
            for next_course in graph[curr_course]:
                indegrees[next_course] -= 1
                
                if indegrees[next_course] == 0:
                    queue.append(next_course)
                
        return len(taken_courses) == numCourses