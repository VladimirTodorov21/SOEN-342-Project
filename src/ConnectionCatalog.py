import csv
from pathlib import Path
from typing import List
from Connection import Connection
from gateways.ConnectionGateway import ConnectionGateway
class ConnectionCatalog:

    
    connection_catalog: List[Connection]=[]
   
    def __init__(self):
        self.readCSV()
   

    def readCSV(self):
        connectionGate=ConnectionGateway()
        connectionGate.hasConnectionTable()
        
        keymap = {
            "Route ID": "routeID",
            "Departure City": "departCity",
            "Arrival City": "arrivalCity",
            "Departure Time": "departTime",
            "Arrival Time": "arrivalTime",
            "Train Type": "trainType",
            "Days of Operation": "daysOperation",
            "First Class ticket rate (in euro)": "firstClassRate",
            "Second Class ticket rate (in euro)": "secondClassRate",
        }
        #adding rows to sqlite only if connection table doesn't have 1200 entries already from csv
        
        CSV = Path(__file__).resolve().parent / "assets" / "eu_rail_network.csv"
        with CSV.open(newline="",encoding='utf-8') as csvfile:
             reader=csv.DictReader(csvfile)
             for row in reader:
                 data = {keymap[key]: row[key] for key in keymap}
                 stub=Connection(**data)
                 self.connection_catalog.append(stub)
                 if (connectionGate.hasConnectionTable==False):
                    connectionGate.addConnection(data)
        connectionGate.closeConnection()
