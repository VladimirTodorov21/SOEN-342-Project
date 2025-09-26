from SearchCriteria import *
from ConnectionCatalog import *
from typing import List

class ConnectionFinder:
    search_criteria: SearchCriteria
    connection_catalog: ConnectionCatalog
    direct_connections:List[Connection]=[]
    multi_stop_connections:List[Connection]=[]

    def __init__(self,search,catalog):
       self.search_criteria=search
       self.connection_catalog=catalog

    def getMultiStopConnections(self):
         pass
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
                 print(f"----------------------------------------\n| {"Criteria":<20}| User Data\n----------------------------------------")
                 print(f"| {"Departure City:":<20}| {connection.departure_city}")
                 print(f"| {"Arrival City:":<20}| {connection.arrival_city}")
                 print(f"| {"Departure Time:":<20}| {connection.departure_time}")
                 print(f"| {"Arrival Time:":<20}| {connection.arrival_time}")
                 print(f"| {"Train Type:":<20}| {connection.train_type}")
                 print(f"| {"Days Of Operation:":<20}| {connection.days_of_operation}")
                 print(f"| {"First Class Price:":<20}| {connection.first_class_price}")
                 print(f"| {"Second Class Price:":<20}| {connection.second_class_price}")
                 print("----------------------------------------\n")

    def getTotalPrice():
        pass
    def getTotalDuration():
        pass