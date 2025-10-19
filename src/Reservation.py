import Traveler
import Ticket
class Reservation:
    traveler: Traveler
    ticket: Ticket
    def __init__(self,traveler):
        self.setTraveler(traveler)
    
    def setTraveler(self,traveler):
        self.traveler=traveler
        
    def setTicket(self,ticket):
        self.ticket=ticket
        
    def getTraveler(self):
        return self.traveler
    
    def getTicket(self):
        return self.ticket