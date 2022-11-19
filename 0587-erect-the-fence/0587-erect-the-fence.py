class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def left_turn(p, r, s):
            return (p[0]-s[0])*(r[1]-s[1]) - (p[1]-s[1])*(r[0]-s[0])

        points = sorted(set(tuple(t) for t in trees))
        if len(points) <= 2:
            return points
            
        upper = []
        lower = []
        
        for p in points:
            while len(upper) > 1 and left_turn(p, upper[-1], upper[-2]) < 0:
                upper.pop()

            upper.append(p)

            while len(lower) > 1 and left_turn(lower[-2], lower[-1], p) < 0:
                lower.pop()

            lower.append(p)

        return set(lower[:-1] + upper[:0:-1])