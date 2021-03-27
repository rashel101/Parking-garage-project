from IPython.display import clear_output as clear

class Parking_Garage():
    """
        Class Parking_Garage will have 3 attributes:
        1. list of total number of tickets in a list
        2. list of total number of parking spaces in a list
        3. a dictionary of current tickets held
    """
    # Initializing the class and its 3 attributes
    def __init__(self, ticket_list = list(range(1,11)), parking_list = list(range(1,11)), current_ticket = {}):
        self.ticket_list = ticket_list
        self.parking_list = parking_list
        self.current_ticket = current_ticket
        
    # Method to start the parking garage simulation  
    def start_garage(self):
            print("These are the tickets/parking spots {} available".format(self.ticket_list))
            while True:
                self.parking_Options()    
                
    # First method to prompt user with the different options in the garage
    def parking_Options(self):
        options = input("What would you like to do? Pay/Park/Leave? ")
        if len(self.ticket_list) == 0 and options.lower() == "park":
            print('Sorry the parking lot is full. Please come back later.')
            return
        elif options.lower() == "park":
            self.takeTicket()
        elif options.lower() == "pay":
            self.pay_Ticket()
        elif options.lower() == "leave":
            self.leave_Garage()
        elif options.lower() not in ('pay', 'park', 'leave'):
            print("Invalid Choice")
            clear()
    
    # Method 2 when the user inputs "park" prompting the user to take a ticket with a parking space attached
    def takeTicket(self):
        user_ticket = int(input(f"Take a number: {self.ticket_list}"))
        if user_ticket not in self.ticket_list:
            print('That ticket is taken. Please choose another ticket.')
        else:
            self.ticket_list.remove(user_ticket)
            self.current_ticket.update({user_ticket: 'NOT PAID'})
            clear()
            print(f"(This is your parking ticket. Please do not lose your ticket! {self.current_ticket})")
    
    # Method 3 when the user inputs "pay" prompting the user to put in their ticket number and "pay"(Changes the dictionary)
    def pay_Ticket(self):
        user_payment = int(input(f"Please enter your ticket number: "))
        if user_payment in self.current_ticket:
            self.current_ticket.update({user_payment: 'PAID'})
            print(f"(Thank you for your payment. Use this updated ticket to leave the garage. {self.current_ticket})")
        else:
            print('You currently do not own that ticket. Please enter the garage and obtain a ticket.')
    
    # Method 4 when the user inputs "leave" prompts the user to put in their ticket number and will either accept or reject
    # depending on whether or not the user has paid for the ticket
    def leave_Garage(self):
        user_exit = int(input(f'Please enter your ticket number: '))
        ticket_check = self.current_ticket.get(user_exit)
        
        if ticket_check == None:
            print("You currently do not own that ticket. Please enter your ticket number to leave or enter the garage to obtain a ticket.")
            self.takeTicket
        elif ticket_check.lower() == "paid":
            print('Thank you for visiting. Have a nice day!')
            self.ticket_list.append(user_exit)
            self.ticket_list.sort()          
        elif ticket_check.lower() == "not paid":
            print('You have not paid for your parking ticket. Please do not forget to pay for your parking ticket!')
            self.parking_Options()
        else:
            print('You currently do not own that ticket. Please enter the garage and obtain a ticket.')
       
          
a = Parking_Garage()
a.start_garage()