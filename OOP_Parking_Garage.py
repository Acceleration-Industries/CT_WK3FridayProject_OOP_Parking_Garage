
class ParkingGarage():
    def __init__(self, parking_spaces_available):
        self.total_tickets_available = 100      
        self.parking_spaces_available = parking_spaces_available
        self.current_ticket = {}
        self.user_response = None      # Not sure if we need this

    
    
    # ** TO DO **
    # Take_Ticket functionality
    #   Decrease the amount of tickets_available by 1 OR decrease the amount of parking_spaces available by 1
    #
    # Pay_for_parking functionality
    #   
    
    
    
    
    
    
    
    # Justin
    def take_ticket(self):
        
        while True:
            if  self.parking_spaces_available >= 1:
                print("Welcome to our Garage!")
                self.user_response = input("Lucky for you, we currently have space available. Would you like a ticket? Yes or No ").title()
                if self.user_response == "Yes":
                    print("Okay, here's your ticket")
                    self.total_tickets_available -= 1
                    print(f"There are {self.total_tickets_available} tickets left.")
                    break
                elif self.user_response == "No":
                    print("Okay have a nice day.")
                else:
                    print("Sorry that is an invalid option.")
            
            else:
                print("Sorry we're currently full. Please come back later.")
                break


    # Will
    def pay_for_parking(self):
        if self.current_ticket in 
        



        if self.user_response == "Yes":
            unpaid_ticket = input("Okay that'll be $20.00")
            self.current_ticket += 1

    
    
     # Razvan
    def leave_garage(self):
        pass




parkinggarage = ParkingGarage(100)
print(parkinggarage.total_tickets_available)
parkinggarage.take_ticket()
print(parkinggarage.total_tickets_available)