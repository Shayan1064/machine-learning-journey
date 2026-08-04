class Dashboard:

    def menu(self, account):

        while True:

            print("\n" + "=" * 50)
            print("              SHAYAN BANK")
            print("=" * 50)

            print(f"Welcome : {account.name}")
            print(f"Account : {account.account_no}")

            print("=" * 50)

            print("1. Show Profile")
            print("2. Show Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Money")
            print("6. Transaction History")
            print("7. Change Password")
            print("8. Logout")

            print("=" * 50)

            choice = input("Enter Your Choice : ")

            if choice == "1":
                account.show_profile()

            elif choice == "2":
                account.show_balance()

            elif choice == "3":
                account.deposit()

            elif choice == "4":
                account.withdraw()

            elif choice == "5":
                print("\n========================================")
                print("Transfer Money")
                print("This feature will be added in Part 4.")
                print("========================================")

            elif choice == "6":
                account.show_history()

            elif choice == "7":
                print("\n========================================")
                print("Change Password")
                print("This feature will be added in Part 5.")
                print("========================================")

            elif choice == "8":
                print("\n========================================")
                print("Thank You For Using SHAYAN BANK")
                print("Logging Out...")
                print("========================================")
                break

            else:
                print("\nInvalid Choice! Please Try Again.")