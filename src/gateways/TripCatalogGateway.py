import sqlite3
from pathlib import Path

class TripCatalogGateway:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parents[2]
        DB_PATH  = BASE_DIR / "src" / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()

        print(f"Connected to database at: {DB_PATH}")


    def getTrips(self,traveler_id,last_name=None):

        query = ("""
                 
            SELECT  trip.trip_code, 
                    trip.status, 
                    reservation.ticketId,
                    traveler.travelerFName, 
                    traveler.travelerLName, 
                    traveler.travelerAge

            FROM trip 
            JOIN reservation ON trip.trip_code = reservation.tripID
            JOIN traveler ON reservation.travelerId = traveler.travelerId                
            WHERE traveler.travelerId = ?  

                 """)
        
        
        self.cur.execute(query,[traveler_id])
        return self.cur.fetchall()
    
    def getTripsStatus(self,traveler_id,last_name,status=None):



        query = ("""
                 
                SELECT  trip.trip_code, 
                        trip.status, 
                        reservation.ticketId,
                        traveler.travelerFName, 
                        traveler.travelerLName, 
                        traveler.travelerAge

                FROM trip 
                JOIN reservation ON trip.trip_code = reservation.tripID
                JOIN traveler ON reservation.travelerId = traveler.travelerId
                WHERE traveler.travelerId = ?   

                 """)
        
        
        
        params = [traveler_id]
        if status:
            query += " AND LOWER(trip.status) = LOWER(?)"
            params.append(status)

        self.cur.execute(query, params)
        return self.cur.fetchall()    
    
    def closeConnection(self):
        self.conn.close()
        
