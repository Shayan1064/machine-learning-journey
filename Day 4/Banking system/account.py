class BankAccount:

    def __init__(self, username, password, name, account_no, phone, email, balance):

        self.username = username
        self.password = password

        self.name = name
        self.account_no = account_no
        self.phone = phone
        self.email = email

        self.balance = balance

        self.attempts = 0
        self.is_blocked = False

        self.history = []

    # ---------------- LOGIN ----------------

    def login(self):

        if self.is_blocked:
            print("\n====================================")
            print("YOUR ACCOUNT IS BLOCKED")
            print("Please Contact the Bank.")
            print("====================================")
            return False

        username = input("Username : ")
        password = input("Password : ")

        if username == self.username and password == self.password:

            self.attempts = 0

            print("\n====================================")
            print("Login Successful")
            print(f"Welcome {self.name}")
            print("====================================")

            return True

        self.attempts += 1

        if self.attempts >= 3:

            self.is_blocked = True

            print("\n====================================")
            print("Too Many Wrong Attempts")
            print("ACCOUNT BLOCKED")
            print("====================================")

        else:

            print("\nWrong Username or Password")
            print("Remaining Attempts :", 3 - self.attempts)

        return False

    # ---------------- PROFILE ----------------

    def show_profile(self):

        print("\n========================================")
        print("           ACCOUNT PROFILE")
        print("========================================")

        print(f"Name           : {self.name}")
        print(f"Account Number : {self.account_no}")
        print(f"Phone          : {self.phone}")
        print(f"Email          : {self.email}")
        print(f"Balance        : Rs. {self.balance}")

        print("========================================")

    # ---------------- BALANCE ----------------

    def show_balance(self):

        print("\n========================================")
        print(f"Current Balance : Rs. {self.balance}")
        print("========================================")

    # ---------------- DEPOSIT ----------------

    def deposit(self):

        amount = float(input("Enter Deposit Amount : "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        self.balance += amount

        self.history.append(
            f"Deposit   | Amount : Rs.{amount} | Balance : Rs.{self.balance}"
        )

        print("\n========================================")
        print("Deposit Successful")
        print(f"Deposited : Rs. {amount}")
        print(f"Balance   : Rs. {self.balance}")
        print("========================================")

    # ---------------- WITHDRAW ----------------

    def withdraw(self):

        amount = float(input("Enter Withdraw Amount : "))

        if amount <= 0:
            print("Invalid Amount!")
            return

        if amount > self.balance:
            print("\nInsufficient Balance!")
            return

        self.balance -= amount

        self.history.append(
            f"Withdraw  | Amount : Rs.{amount} | Balance : Rs.{self.balance}"
        )

        print("\n========================================")
        print("Withdrawal Successful")
        print(f"Withdrawn : Rs. {amount}")
        print(f"Balance   : Rs. {self.balance}")
        print("========================================")

    # ---------------- HISTORY ----------------

    def show_history(self):

        print("\n========================================")
        print("        TRANSACTION HISTORY")
        print("========================================")

        if len(self.history) == 0:
            print("No Transactions Found.")

        else:
            for i, transaction in enumerate(self.history, start=1):
                print(f"{i}. {transaction}")

        print("========================================")