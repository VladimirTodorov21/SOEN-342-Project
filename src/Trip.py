import Reservation
import Connection
from typing import List
from datetime import datetime
from gateways.TripGateway import TripGateway
class Trip:
    trip_id:str #alphanumberic AX
    status:str
    
    def __init__(self,trip_status:str,departure_day: datetime=None):
        self.reservations: List[Reservation.Reservation]=[]
        self.connection: List[Connection.Connection]=[]
        self.departure_day=departure_day if departure_day else datetime.today() 
        self.status=trip_status
    def setID(self,id):
        self.trip_id=id
        
    def addReservation(self,reservation):
        self.reservations.append(reservation)
    
    def addConnection(self,connectionChoice):
        
        self.connection.append(connectionChoice)
        trip_gateway= TripGateway()

        departure_day_str=self.departure_day.strftime("%Y-%m-%d")
        
        if (isinstance(connectionChoice,tuple)):
            directID= (connectionChoice[0].route_ID)
            multiID= connectionChoice[1].route_ID
            tripID=trip_gateway.insertTrip(self.status,directID,multiID)
        else:
            directID=connectionChoice.route_ID
            tripID=trip_gateway.insertTrip(self.status,departure_day_str,directID)
        self.setID("A"+str(tripID))
        trip_gateway.closeConnection()
        
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
    
    def getStatus(self):
        return self.status
    
    def format(self):
        return (f"Trip ID: {self.trip_id},Status:{self.status}, Departure Day:{self.departure_day.strftime('%Y-%m-%d')}")
