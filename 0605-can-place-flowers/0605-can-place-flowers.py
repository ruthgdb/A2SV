class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                before = flowerbed[i - 1] if i > 0 else 0
                after = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
                
                if before == after == 0:
                    flowerbed[i] = 1
                    n -= 1
                    
        return n <= 0