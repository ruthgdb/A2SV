class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(speed))]
        cars.sort()
        distanceLeft = [(target - cars[i][0]) / cars[i][1] for i in range(len(cars))]
        stack = []
        
        for dist in reversed(distanceLeft):
            currMax = dist
            
            while stack and stack[-1] >= currMax:
                currMax = max(currMax, stack.pop())
            
            stack.append(currMax)
        
        return len(stack)