class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        shortest_time = 0 if passengers[0] < 2 else passengers[0] - 1
        j = 0
        
        for i in range(len(buses)):
            cap = 0
            
            while j < len(passengers) and cap < capacity and passengers[j] <= buses[i]:
                if passengers[j - 1] != passengers[j] - 1:
                    shortest_time = passengers[j] - 1
                
                cap += 1
                j += 1
            
            if cap < capacity and (j == 0 or passengers[j - 1] < buses[i]):
                shortest_time = buses[i]
                    
        return shortest_time