class UndergroundSystem:

    def __init__(self):
        self.checkInTime = defaultdict(tuple)
        self.totalTime = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTime[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, startStation = self.checkInTime[id]
        total = t - startTime
        self.totalTime[(startStation, stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.totalTime[(startStation, endStation)]) / len(self.totalTime[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)