from typing import List
from Trip import *
from Traveler import Traveler
from Ticket import Ticket
from catalogs.TicketRecords import TicketRecords
from datetime import datetime
from gateways.TripGateway import TripGateway
from gateways.TripCatalogGateway import TripCatalogGateway
class TripCatalog:
    
    def __init__(self):
        self.trips:List[Trip]=[]
        
    def makeTrip(self,tripStatus):
        
        trip=Trip(tripStatus) #creating a new trip with id = length of trips + 1
        
        
        return trip
        
    def addTrip(self,trip):
        self.trips.append(trip)
 
        
    def getTrips(self):
        return self.trips
    

    def getTravelerTrips(self,traveler_id,last_name,status):

        gateway = TripCatalogGateway()
        rows = gateway.getTripsStatus(traveler_id,last_name,status)
        gateway.closeConnection()

        trips = []

        for code,status,ticket_id,fname,lname,age in rows:
            try:

                
                trip=Trip(status)
                trip.setID(code)

                traveler=Traveler(traveler_id,fname,lname,age)
                reservation=Reservation(traveler)
                ticket=Ticket(ticket_id)
                reservation.setTicket(ticket,trip.getID())
                trip.addReservation(reservation)

                trips.append(trip)

            except ValueError:
                continue


        return trips
    
    def existingReservation(self,traveler_id,trip_id):

        import sqlite3
        connection=sqlite3.connect('src/database/soen342project.db')

        cursor= connection.cursor()
        cursor.execute(""" 

            SELECT COUNT(*) FROM reservation
            where travelerId=? AND tripID=?           

            """, (traveler_id,trip_id))
        
        cnt= cursor.fetchone()[0]
        connection.close()

        return cnt>0
