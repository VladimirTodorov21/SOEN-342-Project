import Reservation
from typing import List
class Trip:
    trip_id:str #alphanumberic AX
    
    
    def __init__(self,id):
        self.id=id
        self.reservations: List[Reservation.Reservation]=[]
    
    def setID(self,id):
        self.trip_id=id
        
    def addReservation(self,reservation):
        self.reservations.append(reservation)
        
    def getID(self):
        return self.trip_id
    
    def getReservation(self):
        return self.reservations