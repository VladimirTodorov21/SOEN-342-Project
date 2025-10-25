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
          trip.addConnection(connectionChoice)
          print(f"\n---Booking a trip for {numTravelers} travelers---\n")
          for i in range(int(numTravelers)):
            fname=input("Input Traveler First Name: ").strip()
            lname=input("Input Traveler Last Name: ").strip()
            age=input("Input Traveler age: ").strip()
            id=len(self.travelerCatalog.getTravelers())+1
            
            traveler=self.travelerCatalog.makeTraveler(id,fname,lname,age)
            print(f"\nReservation Created for {traveler.getFName()} {traveler.getLName()} with Traveler ID: {traveler.getID()}\n")
            reservation=traveler.getReservation()

            ticket=self.ticketRecord.makeTicket(reservation[len(reservation)-1])
            reservation[len(reservation)-1].setTicket(ticket)
            print(f"Ticket created with unique ID {ticket.getID()}\n")
            trip.addReservation(reservation[len(reservation)-1])
        
          self.tripCatalog.addTrip(trip)
          if isinstance(connectionChoice, tuple):
            connection_1, connection_2 = connectionChoice
            print(f"Multi-stop Trip from {connection_1.getDepartureCity()} to {connection_2.getArrivalCity()} has been booked for {numTravelers} travelers!\n")
          else:
            print(f"Direct Trip from {connectionChoice.getDepartureCity()} to {connectionChoice.getArrivalCity()} has been booked for {numTravelers} travelers!\n")

    def viewTrips(self,lname:str,traveler_id:str):
        trip_found= []
        for trip in self.tripCatalog.getTrips(): 
            for reservation in trip.getReservations():
                traveler = reservation.getTraveler()

                if (traveler.getLName().lower()==lname.lower()) and (str(traveler.getID())==traveler_id):
                    trip_found.append((trip,reservation))

        if not(trip_found): 
            print("\nNo trips were found linked to this traveler \n")
            return
                
        present_trip=[]
        past_trip=[]
        today=datetime.today()

        for (trip,reservation) in trip_found: 

            dep_day=trip.getDepartureDay()

            if dep_day.date()< today.date():
                past_trip.append((trip,reservation))
            elif dep_day.date()==today.date():
                present_trip.append((trip,reservation))

        print(f"\n--- The trips that were found for {lname} with ID: {traveler_id} ---\n")

        #current trips
        if present_trip:
            print("Current Trips:\n")
            for trip,reservation in present_trip:
                self.printTrip(trip,reservation)

        #past trips
        if past_trip:
            print("Trip History:\n")
            for trip,reservation in past_trip:
                self.printTrip(trip,reservation)  

        if not(past_trip): 
            print("\n No past trips have been found. Ending view trips.")

    def printTrip(self,trip,reservation):
            ticket=reservation.getTicket()
            traveler=reservation.getTraveler()
            connection=trip.getConnection()

            if isinstance(connection, list) and len(connection) == 1:
                connection_type = connection[0]

                if isinstance(connection_type, tuple) and len(connection_type) == 2:
                    connection = "Multi-Stop Connection from " + connection_type[0].getDepartureCity() + " to " + connection_type[1].getArrivalCity()
                else:
                    connection = "Direct Connection from " + connection_type.getDepartureCity() + " to " + connection_type.getArrivalCity()

            print(f"Trip ID: {trip.getID()}")
            print(f"Ticket ID: {ticket.getID()}") 
            print(f"Traveler: {traveler.getFName()} {traveler.getLName()} (Age: {traveler.getAge()})")
            print(connection)
            print("-------------------------------")


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
                        
                        lname=input("Enter traveler's last name: ").strip()
                        traveler_id=input("Enter traveler's ID:").strip()

                        self.viewTrips(lname,traveler_id)

                        input("Press 'Enter' to go back to the menu: ")

                        menuProceed = False
                        break

                    case "4": # Exiting the System
                        print("\nThank you for using the Railway Network System, Goodbye!")
                        menuProceed = False
                        menu_on = False
          
if __name__ == "__main__":
    main = Main()
    main.run()