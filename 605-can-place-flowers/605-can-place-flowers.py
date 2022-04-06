class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 1 and n == 0:
                return True
            elif flowerbed[0] == 1 and n > 0:
                return False
            elif flowerbed[0] == 0 and n > 1:
                return False
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1
        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            count += 1
            flowerbed[len(flowerbed) - 1] = 1
        
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i + 1] == flowerbed[i - 1] == flowerbed[i]:
                count += 1
                flowerbed[i] = abs(flowerbed[i] - 1)

        if n <= count:
            return True
        return False