from typing import List
class SearchCriteria:
    # Attributes
    departure_city: str
    arrival_city: str
    departure_time: str
    arrival_time: str
    train_type: str
    days_of_operation: List[str]
    first_class_price: float
    second_class_price: float 
    # Default Constructor
    def __init__(self):
        self.departure_city = ""
        self.arrival_city = ""
        self.departure_time = ""
        self.arrival_time = ""
        self.train_type = ""
        self.days_of_operation = [""]
        self.first_class_price = 0.0
        self.second_class_price = 0.0

    # Setter Functions
    def setDepartureCity(self, d_city):
        self.departure_city = d_city

    def setArrivalCity(self, a_city):
        self.arrival_city = a_city
    
    def setDepartureTime(self, d_time):
        if d_time == "":
            self.departure_time = "N/A"
        else:
            self.departure_time = d_time
    
    def setArrivalTime(self, a_time):
        if a_time == "":
            self.arrival_time = "N/A"
        else:
            self.arrival_time = a_time

    def setTrainType(self, t_type):
        if t_type == "":
            self.train_type = "N/A"
        else:
            self.train_type = t_type

    def setDaysOfOperation(self, d_of_operation):
        if d_of_operation:
            if "-" in d_of_operation:
                start, end = [d.strip() for d in d_of_operation.split("-")]
                week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                if start in week and end in week:
                    index_start = week.index(start)
                    index_end = week.index(end)
                    if index_start <= index_end:
                        self.days_of_operation = week[index_start:index_end+1]
                    else:
                        self.days_of_operation = week[index_start:] + week[:index_end+1]
            elif d_of_operation == "Daily":
                self.days_of_operation = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            else:  # e.g. Mon,Tue
                self.days_of_operation = [d.strip() for d in d_of_operation.split(",")]

    def setFirstClassPrice(self, fClassPrice):
        self.first_class_price = fClassPrice

    def setSecondClassPrice(self, sClassPrice):
        self.second_class_price = sClassPrice

    # Getter Functions
    
    def getDepartureCity(self):
        return self.departure_city
    
    def getArrivalCity(self):
        return self.arrival_city
    
    def getDepartureTime(self):
        return self.departure_time
    
    def getArrivalTime(self):
        return self.arrival_time
    
    def getTrainType(self):
        return self.train_type
    
    def getDaysOfOperation(self):
        return self.days_of_operation
    
    def getFirstClassPrice(self):
        return self.first_class_price
    
    def getSecondClassPrice(self):
        return self.second_class_price
    
    ######################################

    def collect_user_input(self):
        
        departure_city = ""
        while True:
            departure_city = input("[Mandatory] Enter your city of departure: ").strip()
            if departure_city != "":
                break
            print("Please try again! Don't leave this field blank\n")
        self.setDepartureCity(departure_city)

        arrival_city = ""
        while True:
            arrival_city = input("[Mandatory] Enter the city in which you wish to arrive: ").strip()
            if arrival_city != "":
                break
            print("Please try again! Don't leave this field blank\n")
        self.setArrivalCity( arrival_city)

        departure_time = input("[Optional] Enter the departure time (HH:MM) or leave blank: ").strip()
        self.setDepartureTime( departure_time)

        arrival_time = input("[Optional] Enter the arrival time (HH:MM) or leave blank: ").strip()
        self.setArrivalTime( arrival_time)

        train_type = input("[Optional] Enter the type of train you wish to embark in or leave blank: ").strip()
        self.setTrainType( train_type)

        days_of_operation = input("[Optional] Enter the train's days of operation (e.g. Mon,Tue | Mon-Tue | Daily) or leave blank: ").strip()
        self.setDaysOfOperation( days_of_operation)

        ticket_choice = input("[Optional] Enter what ticket class price you wish to look for (first or second) or leave blank: ").strip()
        if ticket_choice == "first":
            first_class_price = input("Enter the maximum amount you wish to pay for the first class ticket: ").strip()
            self.setFirstClassPrice( first_class_price)
            self.setSecondClassPrice( 0.0)
        elif ticket_choice == "second":
            second_class_price = input("Enter the maximum amount you wish to pay for the second class ticket: ").strip()
            self.setFirstClassPrice( 0.0)
            self.setSecondClassPrice( second_class_price)
        else:
            self.setFirstClassPrice( 0.0)
            self.setSecondClassPrice( 0.0)
    
    def display_user_input(self):
        print("\nCollected User Search Criteria:")
        print(f"----------------------------------------\n| {"Criteria":<20}| User Data\n----------------------------------------")
        print(f"| {"Departure City:":<20}| {self.getDepartureCity()}")
        print(f"| {"Arrival City:":<20}| {self.getArrivalCity()}")
        print(f"| {"Departure Time:":<20}| {self.getDepartureTime()}")
        print(f"| {"Arrival Time:":<20}| {self.getArrivalTime()}")
        print(f"| {"Train Type:":<20}| {self.getTrainType()}")
        print(f"| {"Days Of Operation:":<20}| {self.getDaysOfOperation()}")
        print(f"| {"First Class Price:":<20}| {self.getFirstClassPrice()}")
        print(f"| {"Second Class Price:":<20}| {self.getSecondClassPrice()}")
        print("----------------------------------------")
