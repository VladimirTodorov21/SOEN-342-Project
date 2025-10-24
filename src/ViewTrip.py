from datetime import datetime

class ViewTrip:
    def __init__(self,tripCatalog): 
        self.tripCatalog=tripCatalog

    def viewTrips(self,lname:str,traveler_id:str):
        trip_found= []
        for trip in self.tripCatalog.getTrips(): 
            for reservation in trip.getReservation():
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


