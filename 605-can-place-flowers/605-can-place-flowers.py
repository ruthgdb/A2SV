class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        if length == 1:
            if flowerbed[0] == 0:
                count += 1
                n -= 1
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                flowerbed[0] = 1
                
            if flowerbed[length - 1] == 0 and flowerbed[length - 2] == 0:
                count += 1
                flowerbed[length - 1] = 1

            for i in range(1, length - 1):
                if flowerbed[i + 1] == flowerbed[i - 1] == flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
         
        return n <= count