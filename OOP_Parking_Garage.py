
class ParkingGarage():
    def __init__(self, parking_spaces_available):
        self.total_tickets_available = 100      
        self.parking_spaces_available = parking_spaces_available
        self.current_ticket = {}
        self.user_response = None      # Not sure if we need this

    
    
    # ** TO DO **
    # 
    #  
    #
   
    
    
    
    
    
    
    # Justin
    def take_ticket(self):
        print("Welcome to our Garage!")
        while True:
            if  self.parking_spaces_available >= 1:
                self.user_response = input("Lucky for you, we currently have space available. Would you like a ticket? Yes or No? ").title()
                if self.user_response == "Yes":
                    print("Okay, here's your ticket")
                    self.total_tickets_available -= 1
                    print(f"There are {self.total_tickets_available} tickets left.")
                    self.current_ticket["Ticket Paid"] = False
                    print(self.current_ticket)
                    break
                elif self.user_response == "No":
                    print("Okay have a nice day.")
                else:
                    print("Sorry that is an invalid option.")
            
            else:
                print("Sorry we're currently full. Please come back later.")
                break




# pay_for_parking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "current_ticket" dictionary key "paid" to True





    # Will
    def pay_for_parking(self):
        print("Thank you for using our parking garage today. Your total will be $20.00")
        self.user_response = input("Please select a PAYMENT METHOD. Press 1 for CASH or 2 for CARD." )
        if self.user_response == '1':
            print("Please insert your CASH.")

        elif self.user_response == '2':
            print("Please swipe your CARD.")

        else:
            ("Sorry that is not a valid option. Please select CASH or CARD.")




        
            # unpaid_ticket = input("Okay that'll be $20.00")
            #     print("Thank you for your payment")
            # self.current_ticket += 1

    




# -leave_garage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parking_spaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)



 
     # Razvan
    def leave_garage(self):
        pass







parkinggarage = ParkingGarage(100)
print(parkinggarage.total_tickets_available)
parkinggarage.take_ticket()
print(parkinggarage.total_tickets_available)