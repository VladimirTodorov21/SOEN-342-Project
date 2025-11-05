import sqlite3
from pathlib import Path

class TripGateway:
    
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        DB_PATH  = BASE_DIR / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
    
    def getNewTripID(self):
        self.cur.execute("SELECT COUNT(*) FROM trip")
        return self.cur.fetchone()[0]
    
 
    def insertTrip(self,status,directID,multiID=""):
        
        row ={
            "status":status,
            "destination":directID,
            "layover":  multiID
        }
        
        self.cur.execute("""
                    INSERT INTO trip
                    (status,directConnectionID,multiStopConnectionID) 
                    VALUES(
                        
                        :status,
                        :destination,
                        :layover
                    )
                        
                         """,row)
        
        self.conn.commit()
        return self.cur.lastrowid
        
    def closeConnection(self):
        self.conn.close()