import Reservation
class Ticket:
    ticket_id:str
    reservation:Reservation
    def __init__(self,id,reservation):
        self.setID(id)
        self.setReservation(reservation)
    
    def setID(self,id):
        self.ticket_id=id
        
    def setReservation(self,reservation):
        self.reservation=reservation
        
    def getID(self):
        return self.ticket_id
    def getReservation(self):
        return self.reservation