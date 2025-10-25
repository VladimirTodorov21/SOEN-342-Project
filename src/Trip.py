import Reservation
import Connection
from typing import List
from datetime import datetime

class Trip:
    trip_id:str #alphanumberic AX
    
    
    def __init__(self,id:str,departure_day: datetime=None):
        self.trip_id=id
        self.reservations: List[Reservation.Reservation]=[]
        self.connection: List[Connection.Connection]=[]
<<<<<<< HEAD
=======
        self.departure_day=departure_day if departure_day else datetime.today() 
>>>>>>> origin/main
    
    def setID(self,id):
        self.trip_id=id
        
    def addReservation(self,reservation):
        self.reservations.append(reservation)
    
    def addConnection(self,connectionChoice):
        self.connection.append(connectionChoice)
        
    def getID(self):
        return self.trip_id
    
    def getReservations(self):
        return self.reservations
    
    def getConnection(self):
        return self.connection
    
    def setDepartureDay(self,dep_day):
        self.departure_day=dep_day

    def getDepartureDay(self):
        return self.departure_day    