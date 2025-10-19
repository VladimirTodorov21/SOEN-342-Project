import Reservation
class Traveler:
    traveler_id: str
    traveler_f_name:str
    traveler_l_name:str
    traveler_age:str
    reservation:Reservation
    def __init__(self,id:str,fname:str,lname:str,age:str):
        self.traveler_id=id
        self.traveler_f_name=fname
        self.traveler_l_name=lname
        self.traveler_age=age
    
    def setID(self,id):
        self.traveler_id=id
        
    def setName(self,name):
        self.traveler_name=name
    
    def setAge(self,age):
        self.traveler_age=age
        
    def getID(self):
        return self.traveler_id
    
    def getFName(self):
        return self.traveler_f_name
    
    def getLName(self):
        return self.traveler_l_name
    
    def getAge(self):
        return self.traveler_age
    
    def getReservation(self):
        return self.reservation

    def createReservation(self):
        self.reservation=Reservation.Reservation(self)
        