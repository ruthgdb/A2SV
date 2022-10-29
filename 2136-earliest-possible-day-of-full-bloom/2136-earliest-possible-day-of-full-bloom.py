class Solution:
    def earliestFullBloom(self, plantTimes: List[int], growTimes: List[int]) -> int:
        bloom_time = [(plantTimes[i], growTimes[i]) for i in range(len(plantTimes))]
        bloom_time.sort(key = lambda x: x[1], reverse = True)
        
        curr_plant_time = 0
        curr_growth_time = 0
        
        for curr_plant, curr_grow in bloom_time:
            curr_plant_time += curr_plant
            curr_growth_time = max(curr_growth_time, curr_plant_time + curr_grow)
            
        return curr_growth_time