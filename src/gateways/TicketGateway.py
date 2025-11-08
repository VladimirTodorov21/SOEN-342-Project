import sqlite3
from pathlib import Path

class TicketGateway:
    
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        DB_PATH  = BASE_DIR / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
    
    def getNewTicketID(self):
        self.cur.execute("SELECT COUNT(*) FROM ticket")
        return self.cur.fetchone()[0]
    
    def insertTicket(self):
       
        self.cur.execute("""
                INSERT INTO ticket DEFAULT VALUES
                """)
        self.conn.commit()
        
        return self.cur.lastrowid
        
        
    def checkReservationForTicket(self,ticketID):
        self.cur.execute("SELECT id FROM reservation WHERE ticketId = :ticketID ",{"ticketID":ticketID})
        row=self.cur.fetchone()

        if row is not None:
            reservation_id=row[0]
            print(f"Ticket {ticketID} linked to reservation {reservation_id}")
            return reservation_id
        else:
            print(f"Ticket {ticketID} not linked to any reservation")
            return None

        
    def closeConnection(self):
        self.conn.close()