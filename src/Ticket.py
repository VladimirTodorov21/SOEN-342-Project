from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Reservation import Reservation
from gateways.TicketGateway import TicketGateway
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
    
    def checkReservationDB(self):
        ticket_gateway=TicketGateway()
        reservation_id= ticket_gateway.checkReservationForTicket(self.ticket_id)
        ticket_gateway.closeConnection()
        return reservation_id