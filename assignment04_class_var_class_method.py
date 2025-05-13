class Bank:
    bank_name = "State Bank"  

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name 

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

customer1 = Bank("Mohammad Umair") 
customer2 = Bank("Adil Hussain")

customer1.display()  
customer2.display()  

Bank.change_bank_name("HBL Bank")

customer1.display()  
customer2.display() 