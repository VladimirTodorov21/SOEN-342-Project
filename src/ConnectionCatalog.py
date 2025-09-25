import csv
from Connection import *
class ConnectionCatalog:

    conection_catalog=list[Connection]
   
    def __init__(self):
        self.readCSV()
   

    def readCSV(self):
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
        with open("./src/assets/eu_rail_network.csv",newline="",encoding='utf-8') as csvfile:
             reader=csv.DictReader(csvfile)
             for row in reader:
                 data = {keymap[key]: row[key] for key in keymap}
                 connection=Connection(**data)
                 self.conection_catalog.append(connection)
                
             


        