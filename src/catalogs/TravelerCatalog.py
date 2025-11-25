from typing import List
from Traveler import *
from gateways.TravelerGateway import TravelerGateway
class TravelerCatalog:
   
    def __init__(self):
        self.travelers:List[Traveler]=[]
    

    def makeTraveler(self,travelerID,traveler_fname:str,traveler_lname:str,traveler_age:str):

        t_gateway=TravelerGateway()
        existingTraveler=t_gateway.checkTraveler(travelerID)
        

        if(existingTraveler):

            existingTraveler_id, existingTraveler_fname, existingTraveler_lname, existingTraveler_age = existingTraveler

            
            if (existingTraveler_fname.lower()==traveler_fname.lower() and existingTraveler_lname.lower()==traveler_lname.lower()
                and str(existingTraveler_age)==str(traveler_age)):

                tr = Traveler(travelerID,traveler_fname,traveler_lname,traveler_age)
                self.add(tr)
                tr.createReservation()
                t_gateway.closeConnection()
                return tr
                    
            else:
                    
                t_gateway.closeConnection()
                raise ValueError(f"This traveler ID {travelerID} already exists. Please try another one.")
            
        
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
    