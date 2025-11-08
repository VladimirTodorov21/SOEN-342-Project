import sqlite3
from pathlib import Path

class TripGateway:
    
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[2]
        DB_PATH  = BASE_DIR / "src" / "database" / "soen342project.db"
        print(f"Connected to database at: {DB_PATH}")

        self.conn = sqlite3.connect(DB_PATH,timeout=10)
        self.cur = self.conn.cursor()


    
 
    def insertTrip(self,status,directID,multiID=""):
        
        row ={
            "status":status,
            "directConnectionID":directID,
            "MultStopConnectionID":  multiID
        }
        
        self.cur.execute("""
                    INSERT INTO trip (status, directConnectionID,multiStopConnectionID) 
                    VALUES(
                        
                        :status,
                        :directConnectionID,
                        :MultStopConnectionID
                        
                    )
                        
                         """,row)
        
        self.conn.commit()
        return self.cur.lastrowid
        
    def closeConnection(self):
        self.conn.close()