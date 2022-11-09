class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        valid_times = []
        
        def count_set(time):
            if time < 2:
                return time
           
            if time % 2 == 0:
                return count_set(time // 2)
             
            return 1 + count_set((time - 1) // 2)
            
        for hour in range(12):
            for minute in range(60):
                if count_set(hour) + count_set(minute) == turnedOn:
                    if minute < 10:
                        valid_times.append(str(hour) + ":" + str(0) + str(minute))
                    else:
                        valid_times.append(str(hour) + ":" + str(minute))

        return valid_times