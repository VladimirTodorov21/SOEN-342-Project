import sqlite3
from pathlib import Path
from Ticket import Ticket
from Traveler import Traveler
class ReservationGateway:
    
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        DB_PATH  = BASE_DIR / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
    
    def getReservationID(self):
        self.cur.execute("SELECT COUNT(*) FROM trip")
        return self.cur.fetchone()[0]
    
 
    def insertReservation(self,ticket:Ticket,traveler:Traveler,tripID):
        travelerID=traveler.getID()
        ticketID=ticket.getID()
        row ={
            "travelerID":travelerID,
            "ticketID":ticketID,
            "tripID":tripID
        }
        self.cur.execute("""
                         INSERT INTO reservation
                         (travelerId,
                         ticketId,tripId)
                         VALUES(
                             :travelerID,
                             :ticketID,
                             :tripID
                         )
                         """,row)
        
        self.conn.commit()
        
    def closeConnection(self):
        self.conn.close()