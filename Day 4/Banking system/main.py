from bank import Bank
from dashboard import Dashboard

bank = Bank()

bank.create_accounts()

dashboard = Dashboard()

while True:

    account = bank.login()

    if account:

        dashboard.menu(account)