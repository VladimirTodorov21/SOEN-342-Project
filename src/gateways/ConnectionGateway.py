import sqlite3
from pathlib import Path

class ConnectionGateway:
    
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parents[1]
        DB_PATH  = BASE_DIR / "database" / "soen342project.db"
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
    
    def hasConnectionTable(self):
        self.cur.execute("SELECT COUNT(*) FROM connection")
        rowCount=self.cur.fetchone()[0]
        if (rowCount==1200):
            return True
        
        return False
        
    def deleteTable(self):
        self.cur.execute("DELETE FROM connection")
    
    def insertConnection(self, connectionObj: dict):
        
        row = {
            "route_id":           connectionObj["routeID"],
            "departure_city":     connectionObj["departCity"],
            "arrival_city":       connectionObj["arrivalCity"],
            "departure_time":     connectionObj["departTime"],
            "arrival_time":       connectionObj["arrivalTime"],
            "train_type":         connectionObj["trainType"],
            "days_of_operation":  connectionObj["daysOperation"],
            "first_class_price":  int(connectionObj["firstClassRate"]),
            "second_class_price": int(connectionObj["secondClassRate"]),
        }

        self.cur.execute("INSERT INTO connection (route_id, departure_city, arrival_city, departure_time, arrival_time,train_type, days_of_operation, first_class_price, second_class_price) VALUES (:route_id, :departure_city, :arrival_city, :departure_time, :arrival_time,:train_type, :days_of_operation, :first_class_price, :second_class_price)", row) 
        self.conn.commit()

        
    def closeConnection(self):
        self.conn.close()