class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topSwaps = 0
        countSame = 0
        for i in range(1, len(tops)):
            if tops[i] == tops[0]:
                countSame += int(tops[i] == bottoms[i])
                continue
                
            if tops[0] == bottoms[i]:
                topSwaps += 1
            else:
                topSwaps = float("inf")
                break
                
        topSwaps = min(topSwaps, abs(len(tops) - topSwaps) - countSame)
                
        bottomSwaps = countSame = 0
        for i in range(1, len(bottoms)):
            if bottoms[i] == bottoms[0]:
                countSame += int(tops[i] == bottoms[i])
                continue
                
            if bottoms[0] == tops[i]:
                bottomSwaps += 1
            else:
                bottomSwaps = float("inf")
                break
                
        bottomSwaps = min(bottomSwaps, abs(len(tops) - bottomSwaps) - countSame)
        return min(topSwaps, bottomSwaps) if min(topSwaps, bottomSwaps) != float("inf") else -1