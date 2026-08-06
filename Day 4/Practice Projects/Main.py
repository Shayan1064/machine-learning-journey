class Bank:
    def __init__(self,name,balance,account_number):
        self.name=name
        self.balance=balance
        self.account_number=account_number
        
    def get_info(self):
        print(f"Name: {self.name}\nAccount Number: {self.account_number}\nBalance: {self.balance}")
    
bank1=Bank("Shayan",100_000,"PK0001")
bank1.get_info()