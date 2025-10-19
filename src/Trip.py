import Reservation
import Connection
from typing import List
class Trip:
    trip_id:str #alphanumberic AX
    
    
    def __init__(self,id):
        self.id=id
        self.reservations: List[Reservation.Reservation]=[]
        self.connection: List[Connection.Connection]=[]
    
    def setID(self,id):
        self.trip_id=id
        
    def addReservation(self,reservation):
        self.reservations.append(reservation)
    
    def addConnection(self,connectionChoice):
        self.connection.append(connectionChoice)
        
    def getID(self):
        return self.trip_id
    
    def getReservation(self):
        return self.reservations