from typing import List

class Connection:
        route_ID: str
        departure_city: str
        arrival_city: str
        departure_time: str
        arrival_time: str
        train_type: str
        days_of_operation: List[str]
        first_class_price: float
        second_class_price: float
        plus_one_day: bool # will be true if arrival time has (+1d) 

        def convertDaysOperation(self,d_of_operation ): # eg: Mon-Wed == [Mon,Tue,Wed]
            if d_of_operation:
                if "-" in d_of_operation:
                    start, end = [d.strip() for d in d_of_operation.split("-")]
                    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    if start in week and end in week:
                        index_start = week.index(start)
                        index_end = week.index(end)
                        if index_start <= index_end:
                            self.days_of_operation = week[index_start:index_end+1]
                        else:
                            self.days_of_operation = week[index_start:] + week[:index_end+1]
                elif d_of_operation == "Daily":
                    self.days_of_operation = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                else:  # e.g. Mon,Tue
                    self.days_of_operation = [d.strip() for d in d_of_operation.split(",")]

        
        def __init__(self,routeID,departCity,arrivalCity,departTime,arrivalTime,trainType,daysOperation,firstClassRate,secondClassRate):
            self.route_ID=routeID
            self.departure_city=departCity
            self.arrival_city=arrivalCity
            self.departure_time=departTime
            
            self.arrival_time=arrivalTime
            self.plus_one_day=False
            if "(+1d)" in self.arrival_time:
                self.arrival_time=self.arrival_time.replace("(+1d)","").strip()
                self.plus_one_day=True


            self.train_type=trainType
            self.first_class_price=float(firstClassRate)
            self.second_class_price=float(secondClassRate)

            self.days_of_operation=[]
            self.convertDaysOperation(daysOperation)
        
        def getDepartureCity(self):
            return self.departure_city
        
        def getArrivalCity(self):
            return self.arrival_city
