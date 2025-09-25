from SearchCriteria import *
from ConnectionCatalog import *

class ConnectionFinder:
    search_criteria: SearchCriteria
    connection_catalog: ConnectionCatalog
    direct_connectons:list[Connection]
    multi_stop_connections:list[Connection]

    def __init__(self,search,catalog):
       self.search_criteria=search
       self.connection_catalog=catalog


    def findDirectConnections(self):
        pass