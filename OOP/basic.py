class atm:
    def __init__(self):
        self.__pin = "" # Making the PIN as private attribute
        self.__balance = 0 
        self.menu()
    def get_pin(self):
        return self.__pin
        
    def set_pin(self,new):
        if(type(new))=='str':
            self.__pin = new
        else:
            print("It's not allowed here. ")
            
    def menu(self):
        while True:
            user_input = int(input("""Enter the choice:
                            Enter 1 to create pin : 
                            Enter 2 to deposit : 
                            Enter 3 to withdraw : 
                            Enter 4 to check balance : 
                            Enter 5 to exit : """))
            
            if user_input==1:
                self.createpin()
            elif user_input==2:
                self.deposit()
            elif user_input==3:
                self.withdraw()
            elif user_input==4:
                self.check()
            else:
                print("BYE! ")
                break
        
    def createpin(self):
                print("Creating the pin : ")
                self.__pin = input("Enter the pin : ")
                print("Pin created successfully.")
            
    def deposit(self):
                temp = input("Enter the pin : ")
                if temp==self.__pin:
                    amount = int(input("Enter the amount : "))
                    self.__balance = self.__balance + amount
                    print("Deposit successful ")
                else :
                    print("Invalid pin")

    def withdraw(self):
                temp = input("Enter the pin : ")
                if temp==self.__pin:
                    amount = int(input("Enter the amount : "))
                    if amount <= self.__balance:
                        self.__balance -= amount
                    else:
                        print("Insufficient balance")
                    print(f"{amount} withdrawn successful available balance is {self.__balance}")
                else :
                    print("Invalid pin")

    def check(self):
        print("The available balance is : {}".format(self.__balance))
        
x = atm()
