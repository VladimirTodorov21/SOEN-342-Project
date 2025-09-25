class Connection:
        route_ID: str
        departure_city: str
        arrival_city: str
        departure_time: str
        arrival_time: str
        train_type: str
        days_of_operation: str
        first_class_price: str
        second_class_price: str

        def __init__(self,routeID,departCity,arrivalCity,departTime,arrivalTime,trainType,daysOperation,firstClassRate,secondClassRate):
            self.route_ID=routeID
            self.departure_city=departCity
            self.arrival_city=arrivalCity
            self.departure_time=departTime
            self.arrival_time=arrivalTime
            self.train_type=trainType
            self.days_of_operation=daysOperation
            self.first_class_price=firstClassRate
            self.second_class_price=secondClassRate