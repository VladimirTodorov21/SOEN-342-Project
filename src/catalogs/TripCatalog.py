from typing import List
from Trip import *
class TripCatalog:
    
    def __init__(self):
        self.trips:List[Trip]=[]
        self.tripConnection=[]
        
    def makeTrip(self):
        trip=Trip("A"+str((len(self.trips)+1))) #creating a new trip with id = length of trips + 1
        return trip
        
    def addTrip(self,trip,connectionChoice):
        self.trips.append(trip)
        self.tripConnection.append(connectionChoice)
    
    def getTrips(self):
        return self.trips
        