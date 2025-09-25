from SearchCriteria import *
from ConnectionCatalog import *
from typing import List

class ConnectionFinder:
    search_criteria: SearchCriteria
    connection_catalog: ConnectionCatalog
    direct_connectons:List[Connection]=[]
    multi_stop_connections:List[Connection]=[]

    def __init__(self,search,catalog):
       self.search_criteria=search
       self.connection_catalog=catalog


    def findDirectConnections(self):
        match = True
        for connection in self.connection_catalog.connection_catalog:
            if (connection.departure_city!=self.search_criteria.departure_city):
                match=False
                continue
            if (connection.arrival_city!=self.search_criteria.arrival_city):
                match=False
                continue
            self.direct_connectons.append(connection)

    def printDirectConnections(self):
        for connection in self.direct_connectons:
            print(connection.route_ID)

    def getTotalPrice():
        pass
    def getTotalDuration():
        pass