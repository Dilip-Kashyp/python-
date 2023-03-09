# Train Ticket Booking Project 


class Train:
    def __init__(self, name, fare, seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def Getstatus(self):
        print(f"Tha name of train is {self.name}.\n This train runs daily form Yamunanagar to Delhi.")
    
    @staticmethod
    def space():
        print("************************")
    
    def Getfare(self):
        print(f" The fare of train is : Rs {self.fare}" )
        
    def Book_Tickets(self):
        if self.seats>0:
            print(f" Your Ticket is successfully Booked.\n Your seat no. is {self.seats}" )
            self.seats=self.seats-1
        else :
            print(f"Sorry , Seats not available. \n Please check or try in Tatkal")
    def traveler(self):
         a=input("Traveler name ")
   



Intercity = Train("Intercity 135021  ",80,4)
#Information of Train info
Intercity.Getstatus()
Intercity.Getfare()
Intercity.space()
#1st Traveler 
Intercity.traveler()
Intercity.Book_Tickets()
Intercity.space()
#2nd Traveler 
Intercity.traveler()
Intercity.Book_Tickets()
Intercity.space()
#3rd Traveler 
Intercity.traveler()
Intercity.Book_Tickets()
Intercity.space()
#4th Traveler 
Intercity.traveler()
Intercity.Book_Tickets()
Intercity.space()
#5th Traveler 
Intercity.traveler()
Intercity.Book_Tickets()
Intercity.space()
#6th Traveler 
Intercity.traveler()
Intercity.Book_Tickets()
Intercity.space()