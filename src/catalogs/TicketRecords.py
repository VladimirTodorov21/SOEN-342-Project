from typing import List
from Ticket import *
import Reservation
from gateways.TicketGateway import TicketGateway
class TicketRecords:
   
    def __init__(self):
        self.tickets: List[Ticket]=[]
        
    def makeTicket(self,reservation:Reservation.Reservation):
        ticket_gateway=TicketGateway()
        ticketID=ticket_gateway.insertTicket()
        ticket_gateway.closeConnection()
        
        
        
        
        ticket=Ticket(ticketID,reservation)
        self.add(ticket)
        return ticket
    
    def add(self,ticket):
        self.tickets.append(ticket)
        
    def getTickets(self):
        return self.tickets