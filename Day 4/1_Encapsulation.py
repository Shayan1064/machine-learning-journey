class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, newBalance):
        self.__balance = newBalance

account1 = BankAccount("Shayan", 12345)

account1.set_balance(200000)

print(f"Name: {account1.name}")
print(f"Balance: {account1.get_balance()}")