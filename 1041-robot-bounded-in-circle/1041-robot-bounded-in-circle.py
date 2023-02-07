class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # L, R
        dirs = {"N": ["W", "E"], "S": ["E", "W"], "E": ["N", "S"], "W": ["S", "N"]}
        start = "N"
        pos = [0, 0]
        
        for instruction in instructions:
            if instruction == 'G':
                if start == "N":
                    pos[1] += 1
                if start == "S":
                    pos[1] -= 1
                if start == "E":
                    pos[0] += 1
                if start == "W":
                    pos[0] -= 1
            if instruction == 'L':
                start = dirs[start][0]
            if instruction == 'R':
                start = dirs[start][1]
        
        return start != 'N' or pos == [0, 0]