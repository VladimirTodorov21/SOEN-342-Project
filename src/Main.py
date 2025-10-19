from SearchCriteria import *
from ConnectionFinder import *
from ConnectionCatalog import *
from catalogs.TicketRecords import TicketRecords
from catalogs.TravelerCatalog import TravelerCatalog
from catalogs.TripCatalog import TripCatalog
import csv
class Main:    
  
  
    def __init__(self):
        self.travelerCatalog = TravelerCatalog()
        self.ticketRecord = TicketRecords()
        self.tripCatalog = TripCatalog()
  
  
    def bookTrip(self,numTravelers): #add Connection(s) here     
          trip=self.tripCatalog.makeTrip()
          print(f"\n---Booking a trip for {numTravelers}---\n")
          for i in range(int(numTravelers)):
            fname=input("Input Traveler First Name: ").strip()
            lname=input("Input Traveler Last Name: ").strip()
            age=input("Input Traveler age: ").strip()
            id=len(self.travelerCatalog.getTravelers())+1
            
            traveler=self.travelerCatalog.makeTraveler(id,fname,lname,age)
            print(f"\nReservation Created for {traveler.getFName()} {traveler.getLName()} with ID: {traveler.getID()}\n")
            reservation=traveler.getReservation()
            ticket=self.ticketRecord.makeTicket(reservation)
            print(f"Ticket created with unique ID {ticket.getID()}\n")
            trip.addReservation(reservation)
            
          self.tripCatalog.addTrip(trip)
          print(f"Trip to (add connection(s) here) has booked for {numTravelers} to !\n")
            

    def run(self):
        #   search = SearchCriteria()
        #   search.collect_user_input()
        #   search.display_user_input()
        #   catalog=ConnectionCatalog()
         
        #   connectionFinder= ConnectionFinder(search,catalog)
        #   connectionFinder.findConnections()
        #   connectionFinder.sortingChoice(search)
        
          numTravelers=input ("How many travelers are you?: ").strip()
          self.bookTrip(numTravelers)
          


if __name__ == "__main__":
    main = Main()
    main.run()