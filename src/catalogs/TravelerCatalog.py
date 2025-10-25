from typing import List
from Traveler import *
class TravelerCatalog:
   
    def __init__(self):
        self.travelers:List[Traveler]=[]
    

    def makeTraveler(self,traveler_id:str,traveler_fname:str,traveler_lname:str,traveler_age:str):
        t=Traveler(traveler_id,traveler_fname,traveler_lname,traveler_age)
        
        for traveler in self.travelers:
            if traveler == t:
                t.createReservation()
                return traveler
        
        self.add(t)
        t.createReservation()
        return t
    
    def add(self,traveler:Traveler):
        self.travelers.append(traveler)
        
    def getTravelers(self):
        return self.travelers