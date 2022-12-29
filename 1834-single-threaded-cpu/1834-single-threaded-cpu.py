class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        heapq.heapify(tasks)
        t = tasks[0][0]
        currTasks = []
        answer = []
        
        while tasks or currTasks:
            while tasks and tasks[0][0] <= t:
                start, time, idx = heapq.heappop(tasks)
                heapq.heappush(currTasks, (time, idx))
            
            if currTasks:
                currTask = heapq.heappop(currTasks)
                answer.append(currTask[1])
                t += currTask[0]
            elif tasks:
                t = tasks[0][0]
                
        return answer