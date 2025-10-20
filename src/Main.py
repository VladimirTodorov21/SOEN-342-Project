from SearchCriteria import *
from ConnectionFinder import *
from ConnectionCatalog import *
from catalogs.TicketRecords import TicketRecords
from catalogs.TravelerCatalog import TravelerCatalog
from catalogs.TripCatalog import TripCatalog
import csv
import os

class Main:    

    def __init__(self):
        self.travelerCatalog = TravelerCatalog()
        self.ticketRecord = TicketRecords()
        self.tripCatalog = TripCatalog()
  
    def bookTrip(self,numTravelers, connectionChoice): #add Connection(s) here     
          trip=self.tripCatalog.makeTrip()
          print(f"\n---Booking a trip for {numTravelers} travelers---\n")
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
            
          self.tripCatalog.addTrip(trip,connectionChoice)
          if isinstance(connectionChoice, tuple):
            connection_1, connection_2 = connectionChoice
            print(f"Multi-stop Trip from {connection_1.getDepartureCity()} to {connection_2.getArrivalCity()} has been booked for {numTravelers} travelers!\n")
          else:
            print(f"Direct Trip from {connectionChoice.getDepartureCity()} to {connectionChoice.getArrivalCity()} has been booked for {numTravelers} travelers!\n")
            
    def run(self):
          search = SearchCriteria()
          catalog=ConnectionCatalog()
          connectionFinder= ConnectionFinder(search,catalog)

          # connectionFinder.clearConnectionChoice()

          menu_on = True

          while(menu_on == True):
              os.system('cls') # clears terminal screen

              print("-----------------------------------------\n| Welcome to the Railway Network System |\n-----------------------------------------")
              print("| 1. Search for Railway Connections\n| 2. Book Trip(s)\n| 3. View Trip(s)\n| 4. Exit\n-----------------------------------------\n")

              menuChoice = input("Please type an integer based on your menu choice above: ").strip()

              menuProceed = True

              while(menuProceed == True):
                match menuChoice:
                    case "1": # Searching for the connection
                        search.collect_user_input()
                        search.display_user_input()

                        connectionFinder.findConnections(search)
                        connectionFinder.printConnections()
                        connectionFinder.sortingChoice(search)
                        connectionFinder.setConnectionChoice()
    
                        proceed = input("Do you wish to proceed with booking a trip? (Yes/No): ")

                        if proceed == "Yes":
                            menuChoice = "2"

                        elif proceed == "No":
                            menuProceed == False
                            break
                        
                    case "2": # Booking a trip
                        if connectionFinder.getConnectionChoice() == []:
                            print("You have no previously chosen connections.\nTo do so, please go back to the menu and select 1 to search for a connection\n")
                        else:
                            if isinstance(connectionFinder.getConnectionChoice(), tuple):
                              connection_1, connection_2 = connectionFinder.getConnectionChoice()
                              print(f"\nPreviously Chosen Multi-stop Trip from {connection_1.getDepartureCity()} to {connection_2.getArrivalCity()}\n")
                            else:
                              print(f"\nPreviously Chosen Direct Trip from {connectionFinder.getConnectionChoice().getDepartureCity()} to {connectionFinder.getConnectionChoice().getArrivalCity()}\n")

                            numTravelers=input ("How many travelers are you?: ").strip()
                            self.bookTrip(numTravelers, connectionFinder.getConnectionChoice())
                        
                        input("Press 'Enter' to go back to menu: ")
                        menuProceed == False
                        break

                    case "3": # Viewing the trips
                        
                        # ********************************
                        # Implement View Trips Method here
                        # ********************************

                        menuProceed = False
                        menu_on = False

                    case "4": # Exiting the System
                        print("\nThank you for using the Railway Network System, Goodbye!")
                        menuProceed = False
                        menu_on = False
          
if __name__ == "__main__":
    main = Main()
    main.run()