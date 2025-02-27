class UndergroundSystem:

    def __init__(self):
        self.travel = {}
        self.history = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        startStation = stationName
        self.travel[id] = (startStation, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        endStation = stationName
        startStation, startTime = self.travel.pop(id)
        key = (startStation, endStation)
        time, count = self.travel.get(key, (0, 0))
        self.travel[key] = (time + (t - startTime), count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        time, count = self.travel.get(key, (0,0))
        return time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)