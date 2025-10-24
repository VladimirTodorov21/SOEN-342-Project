import Reservation
from typing import List
from datetime import datetime

class Trip:
    trip_id:str #alphanumberic AX
    
    
    def __init__(self,id:str,departure_day: datetime=None):
        self.trip_id=id
        self.reservations: List[Reservation.Reservation]=[]
        self.departure_day=departure_day if departure_day else datetime.today() 
    
    def setID(self,id):
        self.trip_id=id
        
    def addReservation(self,reservation):
        self.reservations.append(reservation)
        
    def getID(self):
        return self.trip_id
    
    def getReservations(self):
        return self.reservations
    
    def setDepartureDay(self,dep_day):
        self.departure_day=dep_day

    def getDepartureDay(self):
        return self.departure_day    