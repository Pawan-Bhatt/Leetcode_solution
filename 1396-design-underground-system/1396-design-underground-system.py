class UndergroundSystem:

    def __init__(self):
        self.tripTimes = {}
        self.checkedInCustomers = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedInCustomers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedInCustomers[id]
        del self.checkedInCustomers[id]
        tripTime = t - startTime
        
        if (startStation, stationName) not in self.tripTimes:
            self.tripTimes[(startStation, stationName)] = [tripTime, 1]
        else:
            self.tripTimes[(startStation, stationName)][0] += tripTime
            self.tripTimes[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sumOfTimes, numberOfTrips = self.tripTimes[(startStation, endStation)]
        
        return sumOfTimes / numberOfTrips