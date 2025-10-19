from typing import List
from Ticket import *
import Reservation
class TicketRecords:
   
    def __init__(self):
        self.tickets: List[Ticket]=[]
        
    def makeTicket(self,reservation:Reservation.Reservation):
        ticketID=len(self.tickets)+1
        ticket=Ticket(ticketID,reservation)
        self.add(ticket)
        return ticket
    
    def add(self,ticket):
        self.tickets.append(ticket)
        
    def getTickets(self):
        return self.tickets