import sqlite3
from pathlib import Path
from Traveler import Traveler
class TravelerGateway:
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        DB_PATH  = BASE_DIR / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
    
      
    def insertTraveler(self,traveler:Traveler):

        self.cur.execute("""
                         SELECT 1 FROM traveler WHERE travelerId=?
                         """,(traveler.getID(),))
        if self.cur.fetchone():
            raise ValueError(f"This traveler ID {traveler.getID()} already exists. Please try another one.")

        row = {
        "traveler_id":traveler.getID(),
        "traveler_fname":traveler.getFName(),
        "traveler_lname": traveler.getLName(),
        "traveler_age":   traveler.getAge(),
            }   

        self.cur.execute("""
            INSERT INTO traveler (
                travelerId,
                travelerFName,
                travelerLName,
                travelerAge
            ) VALUES (
                :traveler_id,
                :traveler_fname,
                :traveler_lname,
                :traveler_age
            );
        """, row)

        self.conn.commit()
        return self.cur.lastrowid
    
    def checkTraveler(self,travelerID):
        self.cur.execute("""
                         SELECT * FROM traveler WHERE travelerId=:travelerID
                         """,{"travelerID":travelerID})
        self.conn.commit()
        #print ("User exists")
        
        return self.cur.fetchone()
    
    def setPastTrips(self,travelerID):
        self.cur.execute("""
                         SELECT tripID FROM reservation WHERE travelerId = ?
                         """,(travelerID,))
        
        tripIDs=self.cur.fetchall()
      
        for (trip_id,) in tripIDs:
            self.cur.execute("""
                         UPDATE trip
                         SET status= 'Completed'
                         WHERE trip_code = ?
                           AND status= 'Present'
                         """,(trip_id,))
        
        self.conn.commit()
        
    def closeConnection(self):
        self.conn.close()