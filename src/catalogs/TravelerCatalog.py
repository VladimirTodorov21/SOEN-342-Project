from typing import List
from Traveler import *
from gateways.TravelerGateway import TravelerGateway
class TravelerCatalog:
   
    def __init__(self):
        self.travelers:List[Traveler]=[]
    

    def makeTraveler(self,travelerID,traveler_fname:str,traveler_lname:str,traveler_age:str):
        t_gateway=TravelerGateway()
      
       
        travelerExists=t_gateway.checkTraveler(travelerID)
        
        if(travelerExists):
            t_gateway.setPastTrips(travelerID)
            id=travelerExists[0]
            fname=travelerExists[1]
            lname=travelerExists[2]
            age=travelerExists[3]
            existingTraveler=Traveler(id,fname,lname,age)
            existingTraveler.createReservation()
            self.add(existingTraveler)
            return existingTraveler
        
        # commented out since we use the traveler table to find inputted travelerID  
        # for traveler in self.travelers:
        #     if traveler.getFName().lower() == traveler_fname and traveler.getLName().lower() == traveler_lname and traveler.getAge().lower() == traveler_age:
        #         traveler.createReservation()
        #         #when creating reservation change old trip to past and new one to present
        #         return traveler
        #only creating/inserting if traveler is not found in catalog
        t=Traveler(travelerID,traveler_fname,traveler_lname,traveler_age)
        t_gateway.insertTraveler(t)
        self.add(t)
        t.createReservation()
        t_gateway.closeConnection()
        return t
    
    def add(self,traveler:Traveler):
        self.travelers.append(traveler)
        
    def getTravelers(self):
        return self.travelers