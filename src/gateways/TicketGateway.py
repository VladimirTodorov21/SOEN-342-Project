import sqlite3
from pathlib import Path
from Ticket import Ticket
class TicketGateway:
    
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        DB_PATH  = BASE_DIR / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
        
    def addTrip(self,tripObj:Ticket):
        row ={
            "tripID":tripObj.getID,
            #reservationID
            
        }