from SearchCriteria import *
from ConnectionCatalog import *
from typing import List
from datetime import datetime
from datetime import timedelta

class ConnectionFinder:
    search_criteria: SearchCriteria
    connection_catalog: ConnectionCatalog
    direct_connections:List[Connection]=[]
    multi_stop_connections:List[Connection]=[]

    def __init__(self,search,catalog):
       self.search_criteria=search
       self.connection_catalog=catalog

    def getMultiStopConnections(self):
        for connection_1 in self.connection_catalog.connection_catalog:
            if connection_1.departure_city!=self.search_criteria.departure_city:
                  continue
              
            for connection_2 in self.connection_catalog.connection_catalog:
                if (connection_1.arrival_city==connection_2.departure_city) and (connection_2.arrival_city==self.search_criteria.arrival_city):

                    #Checking for time compatibility
                    if self.duration(connection_1.arrival_time,connection_2.departure_time).total_seconds() <= 0: continue

                    #Payment Filtering
                    if(self.search_criteria.first_class_price!=0.0):
                        if (connection_1.first_class_price + connection_2.first_class_price>self.search_criteria.first_class_price): 
                            continue   

                    if(self.search_criteria.second_class_price!=0.0):
                        if (connection_1.second_class_price + connection_2.second_class_price > self.search_criteria.second_class_price): 
                            continue 
                    
                    self.multi_stop_connections.append((connection_1,connection_2))

        
                    

    def findConnections(self):
        # checking each attribute of a connection if it matches with search_criteria's attributes for direct connections
        for connection in self.connection_catalog.connection_catalog:
            if (connection.departure_city!=self.search_criteria.departure_city):
                continue
            if (connection.arrival_city!=self.search_criteria.arrival_city):
                continue
            if (self.search_criteria.departure_time!="N/A")and (connection.departure_time!=self.search_criteria.departure_time):
                    continue
            if (self.search_criteria.arrival_time!="N/A")and (connection.arrival_time!=self.search_criteria.arrival_time):
                    continue
            if (self.search_criteria.train_type!="N/A") and (connection.train_type!=self.search_criteria.train_type):
                    continue
            if (self.search_criteria.first_class_price!=0.0) and (connection.first_class_price!=self.search_criteria.first_class_price):
                    continue
            if (self.search_criteria.second_class_price!=0.0) and (connection.second_class_price!=self.search_criteria.second_class_price):
                    continue
            if ( self.search_criteria.days_of_operation) and (connection.days_of_operation!=self.search_criteria.days_of_operation):
                   continue
            
            self.direct_connections.append(connection)
        
        #if direct_connections is empty after iterating, call getMultiStopConnections to determine 1/2-stop connections
        if(not self.direct_connections):
             self.getMultiStopConnections()
            

    def printConnections(self):
        if (self.direct_connections):
            print("\n----------Direct Connections------------")
            for index,connection in enumerate(self.direct_connections):
                 print("Connection "+str(index+1)+": ")
                 print(f"----------------------------------------\n| {'Criteria':<20}| User Data\n----------------------------------------")
                 print(f"| {'Departure City:':<20}| {connection.departure_city}")
                 print(f"| {'Arrival City:':<20}| {connection.arrival_city}")
                 print(f"| {'Departure Time:':<20}| {connection.departure_time}")
                 print(f"| {'Arrival Time:':<20}| {connection.arrival_time}")
                 print(f"| {'Train Type:':<20}| {connection.train_type}")
                 print(f"| {'Days Of Operation:':<20}| {connection.days_of_operation}")
                 print(f"| {'First Class Price:':<20}| {connection.first_class_price}")
                 print(f"| {'Second Class Price:':<20}| {connection.second_class_price}")
                 print("----------------------------------------\n")
            print(f"Total Connection Duration: {self.getTotalDuration()}")  
            print(f"Total Amount (First Class): {self.getTotalPrice('first')}")
            print(f"Total Amount (Second Class): {self.getTotalPrice('second')}")   

        if (self.multi_stop_connections): 
            print("\n----------Multiple Connections------------")
            for index,(connection_1, connection_2) in enumerate(self.multi_stop_connections):
                 print("Connection "+str(index+1)+": ")
                 print(f" First Connection: {connection_1.departure_city} -> {connection_1.arrival_city} at {connection_1.departure_time} -> {connection_1.arrival_time}")
                 print(f" Second Connection: {connection_2.departure_city} -> {connection_2.arrival_city} at {connection_2.departure_time} -> {connection_2.arrival_time}")
                 print(f" Amount: {connection_1.first_class_price + connection_2.first_class_price} (First Class)")
                 print(f" Amount: {connection_1.second_class_price + connection_2.second_class_price} (Second Class)")
                 print("----------------------------------------\n")
            print(f"Total Connection Duration: {self.getTotalDuration()}")  
            print(f"Total Amount (First Class): {self.getTotalPrice('first')}")
            print(f"Total Amount (Second Class): {self.getTotalPrice('second')}") 

        if not self.direct_connections and not self.multi_stop_connections:
             print("There are no connections that were found matching your criteria")

                        

    def getTotalPrice(self,class_type="first"):
        if self.direct_connections:
             
            if class_type=="first":
                  return sum(connection.first_class_price for connection in self.direct_connections)
             
            elif class_type=="second":
             return sum(connection.second_class_price for connection in self.direct_connections)
            
        elif self.multi_stop_connections:

            if class_type=="first":
                  return sum(connection_1.first_class_price + connection_2.first_class_price for connection_1,connection_2 in self.multi_stop_connections)
             
            elif class_type=="second":
             return sum(connection_1.second_class_price + connection_2.second_class_price for connection_1,connection_2 in self.multi_stop_connections)    
            
        return 0.0    


    def duration(self,departure,arrival,plus_one_day=False):
         time_format = "%H:%M"
         time_departure=datetime.strptime(departure,time_format)
         time_arrival=datetime.strptime(arrival,time_format)

         if plus_one_day: time_arrival+=timedelta(days=1)
         return (time_arrival - time_departure)
    
    def getTotalDuration(self):
        if self.direct_connections:
             return sum((self.duration(connection.departure_time,connection.arrival_time, connection.plus_one_day)
                        for connection in self.direct_connections),
                    timedelta(0)    
             )
        
        elif self.multi_stop_connections:
             return sum((self.duration(connection_1.departure_time,connection_1.arrival_time,connection_1.plus_one_day)+
                        self.duration(connection_1.arrival_time,connection_2.departure_time)+
                        self.duration(connection_2.departure_time,connection_2.arrival_time,connection_2.plus_one_day)
                        for connection_1,connection_2 in self.multi_stop_connections),

                    timedelta(0))
        
        return timedelta(0)
    
    def sortPrice(self,class_type="first"):
         sort_key=lambda connection: connection.first_class_price if class_type=="first" else connection.second_class_price
         self.direct_connections.sort(key=sort_key)

    def sortDuration(self):
         sort_key=lambda connection: self.duration(connection.departure_time,connection.arrival_time,connection.plus_one_day)
         self.direct_connections.sort(key=sort_key)    

    def sortPriceMultiStop(self,class_type="first"):
         sort_key=lambda both_connections: ( both_connections[0].first_class_price + both_connections[1].first_class_price  
         if class_type=="first" 
         else both_connections[0].second_class_price + both_connections[1].second_class_price
        ) 
         self.multi_stop_connections.sort(key=sort_key)

    def sortDurationMultiStop(self):
         sort_key=lambda both_connections: (
              self.duration(both_connections[0].departure_time,both_connections[0].arrival_time,both_connections[0].plus_one_day)+
              self.duration(both_connections[1].departure_time,both_connections[1].arrival_time,both_connections[1].plus_one_day)
        )
         self.multi_stop_connections.sort(key=sort_key)     
            
            