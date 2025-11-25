from SearchCriteria import *
from ConnectionCatalog import *
from typing import List
from datetime import datetime
from datetime import timedelta

class ConnectionFinder:
    search_criteria: SearchCriteria
    connection_catalog: ConnectionCatalog

    def __init__(self,search,catalog):
       self.search_criteria=search
       self.connection_catalog=catalog
       self.direct_connections=[]
       self.multi_stop_connections=[]
       self.connectionChoice:List[Connection]=[]

    def setConnectionChoice(self):
          
          if not self.direct_connections and not self.multi_stop_connections:
               return

          connectionTypeChoice = ""
          while True:
               connectionTypeChoice = input("Choose your connection ('d' for direct connection or 'm' for multistop connection): ")
               if connectionTypeChoice == "d" or connectionTypeChoice == "m":
                    break
               print("Please try again by giving the correct input!")
          
          if connectionTypeChoice == "d":
               if len(self.direct_connections) != 0:
                    directConnectionChoice = ""
                    while True:
                         directConnectionChoice = input("Choose a direct connection by typing an integer: ")
                         if int(directConnectionChoice) <= len(self.direct_connections) and int(directConnectionChoice) > 0:
                              break
                         print("Please try again by giving the correct input!")

                    self.connectionChoice = self.direct_connections[int(directConnectionChoice)-1]
                    print(f"\nYou have chosen direct connection {directConnectionChoice}\n")
               else:
                    print("There are no direct connections to choose from")

          if connectionTypeChoice == "m":
               if len(self.multi_stop_connections) != 0:
                    multistopConnectionChoice = ""
                    while True:
                         multistopConnectionChoice = input("Choose a multistop connection by typing an integer: ")
                         if int(multistopConnectionChoice) <= len(self.multi_stop_connections) and int(multistopConnectionChoice) > 0:
                              break
                         print("Please try again by giving the correct input!")

                    self.connectionChoice = self.multi_stop_connections[int(multistopConnectionChoice)-1]
                    print(f"\nYou have chosen multi-stop connection {multistopConnectionChoice}\n")
               else:
                    print("There are no multi-stop connections to choose from")

    def getConnectionChoice(self):
        return self.connectionChoice
    
    def clearConnectionChoice(self):
        self.connectionChoice.clear()


    def getMultiStopConnections(self):
        for connection_1 in self.connection_catalog.connection_catalog:
            if connection_1.departure_city!=self.search_criteria.departure_city:
                  continue
              
            for connection_2 in self.connection_catalog.connection_catalog:
                if (connection_1.arrival_city==connection_2.departure_city) and (connection_2.arrival_city==self.search_criteria.arrival_city):

                    #Checking for time compatibility
                    if self.duration(connection_1.arrival_time,connection_2.departure_time).total_seconds() <= 0: continue

                    #Payment Filtering
                    if(self.search_criteria.first_class_price!=0.0):
                        if (connection_1.first_class_price + connection_2.first_class_price>self.search_criteria.first_class_price): 
                            continue   

                    if(self.search_criteria.second_class_price!=0.0):
                        if (connection_1.second_class_price + connection_2.second_class_price > self.search_criteria.second_class_price): 
                            continue 
                    
                    self.multi_stop_connections.append((connection_1,connection_2))

        
                    

    def findConnections(self, criteria):
        self.direct_connections=[]
        self.multi_stop_connections=[]

        # checking each attribute of a connection if it matches with search_criteria's attributes for direct connections
        for connection in self.connection_catalog.connection_catalog:
            if (connection.departure_city.strip().lower()!=self.search_criteria.departure_city.strip().lower()):
                continue
            if (connection.arrival_city.strip().lower()!=self.search_criteria.arrival_city.strip().lower()):
                continue
            if (criteria.departure_time!="N/A")and (connection.departure_time!=criteria.departure_time):
                    continue
            if (criteria.arrival_time!="N/A")and (connection.arrival_time!=criteria.arrival_time):
                    continue
            if (criteria.train_type!="N/A") and (connection.train_type.strip().lower()!=criteria.train_type.strip().lower()):
                    continue
            if (criteria.first_class_price>0.0) and (connection.first_class_price>criteria.first_class_price):
                    continue
            if (criteria.second_class_price>0.0) and (connection.second_class_price>criteria.second_class_price):
                    continue
            
            dayRoute = self.parseDay(connection.days_of_operation)
            if (criteria.days_of_operation) and not any(day in dayRoute for day in criteria.days_of_operation):
                   continue
            
            self.direct_connections.append(connection)
        
        self.getMultiStopConnections()

    def parseDay(self, days_str):
          days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

          if isinstance(days_str,list):
               return [d.strip() for d in days_str]

          if days_str=="Daily":
               return days
          elif "-" in days_str:
             first_index=days.index(start)
             second_index=days.index(end)
             start,end = [d.strip() for d in days_str.split("-")]

             return days[first_index:second_index+1] if first_index<=second_index else days[first_index:]+days[:second_index+1]
          else:
             return [d.strip() for d in days_str.split(",")]

    def printConnections(self):
        if (self.direct_connections):
            print("\n----------Direct Connections------------")
            for index,connection in enumerate(self.direct_connections):
                 print("Connection "+str(index+1)+": ")
                 print(f"----------------------------------------\n| {'Criteria':<20}| User Data\n----------------------------------------")
                 print(f"| {'Departure City:':<20}| {connection.departure_city}")
                 print(f"| {'Arrival City:':<20}| {connection.arrival_city}")
                 print(f"| {'Departure Time:':<20}| {connection.departure_time}")
                 print(f"| {'Arrival Time:':<20}| {connection.arrival_time}")
                 print(f"| {'Train Type:':<20}| {connection.train_type}")
                 print(f"| {'Days Of Operation:':<20}| {connection.days_of_operation}")
                 print(f"| {'First Class Price:':<20}| {connection.first_class_price}")
                 print(f"| {'Second Class Price:':<20}| {connection.second_class_price}")
                 connection_duration=self.duration(connection.departure_time,connection.arrival_time,getattr(connection,'plus_one_day',False))
                 print(f"| {'Total Connection Duration:':<20}| {connection_duration}")  
                 print("----------------------------------------\n") 

        if (self.multi_stop_connections): 
            print("\n----------Multiple Connections------------")
            for index,(connection_1, connection_2) in enumerate(self.multi_stop_connections):
                 print("Connection "+str(index+1)+": ")
                 print(f" First Connection: {connection_1.departure_city} -> {connection_1.arrival_city} at {connection_1.departure_time} -> {connection_1.arrival_time}")
                 print(f" Second Connection: {connection_2.departure_city} -> {connection_2.arrival_city} at {connection_2.departure_time} -> {connection_2.arrival_time}")
                 print(f" Amount: {connection_1.first_class_price + connection_2.first_class_price} (First Class)")
                 print(f" Amount: {connection_1.second_class_price + connection_2.second_class_price} (Second Class)")
                 connection_total_duration=self.duration(connection_1.departure_time,connection_1.arrival_time,connection_1.plus_one_day)+ \
                                           self.duration(connection_1.arrival_time,connection_2.departure_time)+ \
                                           self.duration(connection_2.departure_time,connection_2.arrival_time,connection_2.plus_one_day)
                 print(f"Total Connection Duration: {connection_total_duration}")  
                 print("----------------------------------------\n")

        if not self.direct_connections and not self.multi_stop_connections:
             print("No connections found matching your criteria. Please try again with different criteria.\n")
             return

                    


    def duration(self,departure,arrival,plus_one_day=False):
         time_format = "%H:%M"
         time_departure=datetime.strptime(departure,time_format)
         time_arrival=datetime.strptime(arrival,time_format)

         if plus_one_day: time_arrival+=timedelta(days=1)
         return (time_arrival - time_departure)
    
    
    def sorting(self, by="price", class_type ="first"):

         print(f"Connections are being sorted by '{by}' " + (f" using class type: '{class_type}' for pricing." if by=="price" else "."))

         if by=="price":
              self.direct_connections.sort(
                   key =lambda c: c.first_class_price if class_type== "first" else c.second_class_price #direct connections PRICE
                                           
                                           )  
              self.multi_stop_connections.sort(
                   key=lambda c:(c[0].first_class_price+c[1].first_class_price
                                 if class_type=="first"
                                 else c[0].second_class_price+c[1].second_class_price) #multi-stop connections PRICE
              ) 

         elif by=="duration":      
               self.direct_connections.sort(
                    key=lambda c: self.duration(c.departure_time,c.arrival_time,c.plus_one_day) #direct connections DURATION
               )
               
               self.multi_stop_connections.sort(
                    key=lambda c: (self.duration(c[0].departure_time,c[0].arrival_time,c[0].plus_one_day)+self.duration(c[1].departure_time,c[1].arrival_time,c[1].plus_one_day)) #multi-stop connections DURATION
               )

    def sortingChoice(self,search):
        connection_options=len(self.direct_connections)+len(self.multi_stop_connections)
        if connection_options==0:
               return

        if connection_options>1:
               print("\nThere are multiple connection options for your criteria. Which sort option do you want?")
               print("1. Sort by Price")
               print("2. Sort by Duration")
               choice=input("Enter 1 or 2: ").strip()

               if choice=="1":
                    if search.first_class_price!=0.0:
                         sorting_class="first"
                    elif search.second_class_price!=0.0:
                         sorting_class="second"
                    else:
                         sorting_class="first"

                    self.sorting(by="price",class_type=sorting_class)
               elif choice=="2":
                    self.sorting(by="duration")           
               else:
                    print("Invalid sort option.")
   
        else:
               
            print("\nOnly one connection option found, no sorting needed.")        

        self.printConnections()           
            
            