from typing import List
from Trip import *
from datetime import datetime

class TripCatalog:
    
    def __init__(self):
        self.trips:List[Trip]=[]
        self.tripConnection=[]
        
    def makeTrip(self):
        trip=Trip("A"+str((len(self.trips)+1))) #creating a new trip with id = length of trips + 1
        return trip
        
    def addTrip(self,trip,connectionChoice):
        self.trips.append(trip)
        self.tripConnection.append(connectionChoice)
    
    def getTrips(self):
        return self.trips
    
    def viewTrips(self,lname:str,traveler_id:str):
        trip_found= []
        for trip in self.getTrips(): 
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

            print(f"Trip ID: {trip.getID()}")
            print(f"Ticket ID: {ticket.getID()}") 
            print(f"Traveler: {traveler.getFName()} {traveler.getLName()} (Age: {traveler.getAge()})") 
            print("-------------------------------")  
        