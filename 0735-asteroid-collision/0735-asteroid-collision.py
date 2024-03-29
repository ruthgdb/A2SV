class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i, asteroid in enumerate(asteroids):
            if asteroid > 0 or not stack:
                stack.append(asteroid)
            else:
                should_add = True
                
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                    else:
                        if stack[-1] == abs(asteroid):
                            stack.pop()
                        should_add = False
                        break
                        
                if should_add:
                    stack.append(asteroid)
        
        return stack