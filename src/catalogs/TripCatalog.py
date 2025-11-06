from typing import List
from Trip import *
from catalogs.TicketRecords import TicketRecords
from datetime import datetime
from gateways.TripGateway import TripGateway
class TripCatalog:
    
    def __init__(self):
        self.trips:List[Trip]=[]
        
    def makeTrip(self,tripStatus):
        
        trip=Trip(tripStatus) #creating a new trip with id = length of trips + 1
        
        
        return trip
        
    def addTrip(self,trip):
        self.trips.append(trip)
 
        
    
    def getTrips(self):
        return self.trips
    