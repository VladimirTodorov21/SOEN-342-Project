from TrainConnection import TrainConnection
import csv 

with open('./assets/eu_rail_network.csv',newline='') as csvfile:

    reader = csv.DictReader(csvfile)
    connections=[]
    for row in reader:
        connections.append(row)

    for data in connections:
        print(data)