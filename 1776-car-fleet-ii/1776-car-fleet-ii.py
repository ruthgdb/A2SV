class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        answer = [-1] * len(cars)
        
        for i in range(len(cars) - 1, -1, -1):
            position, speed = cars[i]
            
            while stack and (stack[-1][1] >= speed or (answer[stack[-1][2]] != -1 and answer[stack[-1][2]] < (stack[-1][0] - position) / (speed - stack[-1][1]))):
                stack.pop()
                
            if stack:
                answer[i] = (stack[-1][0] - position) / (speed - stack[-1][1])
                
            stack.append((position, speed, i))
                
        return answer