from account import BankAccount


class Bank:

    def __init__(self):

        self.accounts = []

    # ---------------- CREATE DEFAULT ACCOUNTS ----------------

    def create_accounts(self):

        self.accounts.append(
            BankAccount(
                "Shayan",
                "1234",
                "Shayan Hassan",
                "PK10001",
                "03001234567",
                "shayan@gmail.com",
                50000
            )
        )

        self.accounts.append(
            BankAccount(
                "Noman",
                "1111",
                "Noman Khan",
                "PK10002",
                "03111234567",
                "noman@gmail.com",
                30000
            )
        )

        self.accounts.append(
            BankAccount(
                "Ali",
                "2222",
                "Ali Ahmad",
                "PK10003",
                "03221234567",
                "ali@gmail.com",
                25000
            )
        )

    # ---------------- LOGIN ----------------

    def login(self):

        username = input("Username : ")
        password = input("Password : ")

        for account in self.accounts:

            if account.is_blocked:
                continue

            if account.username == username and account.password == password:

                account.attempts = 0

                print("\nLogin Successful")
                return account

            elif account.username == username:

                account.attempts += 1

                if account.attempts >= 3:

                    account.is_blocked = True

                    print("Account Blocked")

                else:

                    print("Wrong Password")
                    print("Remaining Attempts :", 3-account.attempts)

                return None

        print("Invalid Username")

        return None

    # ---------------- FIND ACCOUNT ----------------

    def find_account(self, account_no):

        for account in self.accounts:

            if account.account_no == account_no:
                return account

        return None