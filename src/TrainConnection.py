class TrainConnection:
    def __init__(self,routeID,departCity,arrivalCity,departTime,arrivalTime,trainType,daysOperation,firstClassRate,secondClassRate):
        self.routeID=routeID
        self.departCity=departCity
        self.arrivalCity=arrivalCity
        self.departTime=departTime
        self.arrivalTime=arrivalTime
        self.trainType=trainType
        self.daysOperation=daysOperation
        self.firstClassRate=firstClassRate
        self.secondClassRate=secondClassRate


    def printAll(self):
        print(self.arrivalCity)
        