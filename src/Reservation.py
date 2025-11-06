from Ticket import Ticket
import Traveler
from gateways.ReservationGateway import ReservationGateway
class Reservation:
    traveler: Traveler
    ticket: Ticket
    def __init__(self,traveler):
        self.traveler = traveler
    
    def setTraveler(self,traveler):
        self.traveler=traveler
        
    def setTicket(self,ticket,tripID):
        # insert reservation into db with ticket and tripID
        reservation_gateway=ReservationGateway()
        reservation_gateway.insertReservation(ticket,self.getTraveler(),tripID)
        self.ticket=ticket
        
    def getTraveler(self):
        return self.traveler
    
    def getTicket(self) -> Ticket: 
        return self.ticket