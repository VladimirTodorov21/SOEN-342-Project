from SearchCriteria import *
from ConnectionFinder import *
from ConnectionCatalog import *
from catalogs.TicketRecords import TicketRecords
from catalogs.TravelerCatalog import TravelerCatalog
from catalogs.TripCatalog import TripCatalog
from gateways.TripGateway import TripGateway
from gateways.TripCatalogGateway import TripCatalogGateway
from catalogs.TravelerCatalog import TravelerCatalog
import csv
import os
import sqlite3



class Main:    

    def __init__(self):
        self.travelerCatalog = TravelerCatalog()
        self.ticketRecord = TicketRecords()
        self.tripCatalog = TripCatalog()
        
  
    def bookTrip(self,numTravelers, connectionChoice,tripStatus): #add Connection(s) here    

        trip=self.tripCatalog.makeTrip(tripStatus)
        trip_gateway= TripGateway()
        trip_id= trip_gateway.insertTrip(status=tripStatus,
                                       directID=connectionChoice.route_ID if not isinstance(connectionChoice, tuple) else connectionChoice[0].route_ID,
                                       multiID =connectionChoice[1].route_ID if isinstance(connectionChoice, tuple) else None
                                           )
        trip.setID(trip_id)

        travelerCatalog=TravelerCatalog()
        
        #insert trip into DB and setting trip ID here
        trip.addConnection(connectionChoice)
        print(f"\n---Booking a trip for {numTravelers} travelers---\n")

        for i in range(int(numTravelers)):
            while True:
                fname=input("Input Traveler First Name: ").strip()
                lname=input("Input Traveler Last Name: ").strip()
                age=input("Input Traveler age: ").strip()
                travelerID=input("Input Traveler ID:").strip()

                #check for duplication of traveler ID in DB and catalog
                try:
                    traveler = travelerCatalog.makeTraveler(travelerID,fname,lname,age)
                    print(f"\nTraveler {fname} {lname} with ID {travelerID} created successfully.\n")
                
                except ValueError as er:
                    print(str(er))
                    continue

                #check reservation duplication
                if self.tripCatalog.existingReservation(travelerID,trip.getID()):
                    print(f"A reservation has already been created witht this traveler ID: {travelerID}. Please try again with a different ID.\n")
                    continue

                reservation=traveler.getReservation()

                #creating a new ticketID here and
                ticket=self.ticketRecord.makeTicket(reservation[len(reservation)-1])
                
                #inserting resrevation into DB
                reservation[len(reservation)-1].setTicket(ticket,trip.getID())
                print(f"Ticket created with unique ID {ticket.getID()}\n")

                cursor=trip_gateway.conn.cursor()
                try:
                    cursor.execute(""" 
                                
                        INSERT INTO reservation (travelerId, ticketId, tripID)
                        VALUES (?,?,?)

                    """, (travelerID,ticket.getID(),trip.getID()))

                    print(f"reservation created for traveler: {travelerID} on trip: {trip.getID()}\n")

                except sqlite3.IntegrityError:

                    print("Traveler already has a reservation for this trip.")   

                trip_gateway.conn.commit()
                
                trip.addReservation(reservation[len(reservation)-1])

                break
            
        self.tripCatalog.addTrip(trip)
        if isinstance(connectionChoice, tuple):
            connection_1, connection_2 = connectionChoice
            print(f"Multi-stop Trip from {connection_1.getDepartureCity()} to {connection_2.getArrivalCity()} has been booked for {numTravelers} travelers!\n")
        else:
            print(f"Direct Trip from {connectionChoice.getDepartureCity()} to {connectionChoice.getArrivalCity()} has been booked for {numTravelers} travelers!\n")

    def viewTrips(self,lname:str,traveler_id:str):

        """ Print trips depending on status of booked trip by traveler """

        lname=lname.strip()
        traveler_id=traveler_id.strip()

        gateway=TripCatalogGateway()
        rows= gateway.getTripsStatus(traveler_id,lname)
        gateway.closeConnection()

        

        if not rows:
            print(f"No traveler found with ID: {traveler_id} and last name {lname}\n")
            return


        trip_status={
            "Completed": "Past Trips",
            "Present": "Present Trips",
            "Future": "Future Trips"}
        
        trip_exist=False

        for db_status,label in trip_status.items():

            print(f"\n--- {label} ---\n")

            exist=False

            for trip_code,status,ticket_id,fname,lname,age in rows:

                if status.lower()==db_status.lower():
                    exist=True
                    trip_exist=True
                    print(f"Trip ID: {trip_code}")
                    print(f"Ticket ID: {ticket_id}")
                    print(f"Traveler: {fname} {lname} (Age: {age})")   
                    print("--------------------------")

            if not exist:
                print(f"No {label.lower()} trips found.") 

        if not (trip_exist):
            print("No trips found for this traveler.\n")

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
              #os.system('cls') # clears terminal screen

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

                        if not connectionFinder.direct_connections and not connectionFinder.multi_stop_connections:
                            break

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
                            print("Are you planning a trip or starting it now?")
                            print("1. Going now")
                            print("2. Planning a future trip")
                            status={
                                "1":"Present",
                                "2":"Future",
                            }
                            travel_status=""
                            while True:
                                choice= input ("Input Choice :").strip()
                                if choice in status:
                                    travel_status=status[choice]
                                    break
                                else:
                                    print("Invalid Option, try again")
                            numTravelers=input ("How many travelers are you?: ").strip()
                            self.bookTrip(numTravelers, connectionFinder.getConnectionChoice(),travel_status)
                        
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