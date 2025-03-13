import random
import csv
import os
from decimal import Decimal

global global_id
global_id = 10001

customers = [
    {'a_id': 10001, 'first_name': 'suresh', 'last_name': 'sigera', 'password': '1', 'balance_checking': None, 'balance_saving': 10000, 'overdraft_count': 0, "active": True},
    {'a_id': 10002, 'first_name': 'james', 'last_name': 'taylor', 'password': '2', 'balance_checking': 0, 'balance_saving': 0, 'overdraft_count': 0, "active": True},
    {'a_id': 10003, 'first_name': 'melvin', 'last_name': 'gordon', 'password': 'uYWE732g4ga1', 'balance_checking': 2000, 'balance_saving': 20000, 'overdraft_count': 0, "active": True},
    {'a_id': 10004, 'first_name': 'stacey', 'last_name': 'abrams', 'password': 'DEU8_qw3y72$', 'balance_checking': 2000, 'balance_saving': 20000, 'overdraft_count': 0, "active": True},
    {'a_id': 10005, 'first_name': 'jake', 'last_name': 'paul', 'password': 'd^dg23g)@', 'balance_checking': 100000, 'balance_saving': 100000, 'overdraft_count': 0, "active": True}
]

fieldnames = ["a_id", "first_name", "last_name", "password", "balance_checking", "balance_saving", "overdraft_count", "active"]

if not os.path.exists("./bank.csv"):
    with open("./bank.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customers:
                writer.writerow(row)
                if int(row["a_id"]) > global_id:
                    global_id = row["a_id"]
        except csv.Error as e:
            print(e)


class Bank:
    def __init__(self):
        self.customers = []

    def load_data(self):
        try:
            global global_id
            with open("bank.csv", "r") as file:
                data = csv.DictReader(file)
                for row in data:
                    if int(row["a_id"]) > global_id:
                        global_id = int(row["a_id"])
                    row['a_id'] = int(row['a_id'])
                    row['active'] = True if row['active'] == 'True' else False
                    row['balance_checking'] = None if row['balance_checking'] == "" else int(row['balance_checking'])
                    row['balance_saving'] = None if row['balance_saving'] == "" else int(row['balance_saving'])
                    row['overdraft_count'] = int(row['overdraft_count'])
                    self.customers.append(row)
        except csv.Error as e:
            print(e)

    def write_csv(self):
        global global_id
        with open("./bank.csv", 'w', newline='') as csvfile:
            try:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in self.customers:
                    writer.writerow(row)
                    if int(row["a_id"]) >= global_id:
                        global_id = row["a_id"]
            except csv.Error as e:
                print(e)

    def add_customer(self, customer):
        self.customers.append({
            'a_id': int(customer.a_id),
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'password': customer.password,
            'balance_checking': customer.balance_checking,
            'balance_saving': customer.balance_saving,
            'active': customer.active,
            'overdraft_count': customer.overdraft_count
        })
        self.write_csv()
        print(f"Account for {customer.first_name} {customer.last_name} added successfully!")

    def login(self):
        a_id = input("Your registered Account ID? ")
        c_pw = input("Your password? ")
        for row in self.customers:
            if a_id == str(row['a_id']) and c_pw == row['password']:
                print(f"Hey, {row['first_name']}! Welcome back.")
                return row
        print("The login details are not valid.")

    def transfer_from_checking_to_saving(self, customer, amount):
        amount = Decimal(amount)
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if customer['balance_checking'] < amount:
            print("Insufficient balance in checking account.")
            return

        customer['balance_checking'] -= amount
        customer['balance_saving'] += amount

        print(f"Successfully transferred {amount} from checking to saving.")
        print(f"New Checking Account Balance: {customer['balance_checking']}")
        print(f"New Savings Account Balance: {customer['balance_saving']}")
        self.write_csv()

    def transfer_from_saving_to_checking(self, customer, amount):
        amount = Decimal(amount)
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if customer['balance_saving'] < amount:
            print("Insufficient balance in savings account.")
            return

        customer['balance_saving'] -= amount
        customer['balance_checking'] += amount

        print(f"Successfully transferred {amount} from savings to checking.")
        print(f"New Checking Account Balance: {customer['balance_checking']}")
        print(f"New Savings Account Balance: {customer['balance_saving']}")
        self.write_csv()

    def transfer_from_account_to_account(self, customer, recipient, amount):
        amount = Decimal(amount)
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if customer['balance_checking'] < amount:
            print("Insufficient balance in checking account.")
            return

        customer['balance_checking'] -= amount
        recipient['balance_checking'] += amount

        print(f"Successfully transferred {amount} from {customer['first_name']} to {recipient['first_name']}.")
        print(f"New Checking Account Balance for {customer['first_name']}: {customer['balance_checking']}")
        print(f"New Checking Account Balance for {recipient['first_name']}: {recipient['balance_checking']}")
        
        for c in self.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_checking'] = customer['balance_checking']
            if c['a_id'] == recipient['a_id']:
                c['balance_checking'] = recipient['balance_checking']

        self.write_csv()


class Customer(Bank):
    def __init__(self, first_name, last_name, password, balance_checking, balance_saving, active, overdraft_count):
        global global_id
        global_id += 1
        self.a_id = int(global_id)
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_saving = balance_saving
        self.active = True
        self.overdraft_count = overdraft_count

    def display_customer_fieldnames(self):
        print("customer fieldnames: a_id, first_name, last_name, password, balance_checking, balance_saving")

    def display_customer(self, customer):
        print(f"ID of Account: {customer['a_id']}.")
        print(f"First Name of Customer: {customer['first_name']}")
        print(f"Last Name of Customer: {customer['last_name']}")
        print(f"Checking Balance of Customer: {customer['balance_checking']}")
        print(f"Savings Balance of Customer: {customer['balance_saving']}")


class Checking_account:
    def __init__(self):
        self.balance = Decimal('0.00')

    def deposit(self, customer, amount, bank):
        amount = Decimal(amount)
        customer['balance_checking'] += amount
        print(f"deposited {amount}. new balance is: {customer['balance_checking']}")

        if customer['balance_checking'] >= 0 and customer['active'] == False:
            print("Account has been reactivated as the balance is now positive.")
            customer['active'] = True  # Reactivate account

        for c in bank.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_checking'] = customer['balance_checking']
        bank.write_csv()

    def can_withdraw(self, customer, amount):
        if customer["active"] == False:
            return [False, "Account is deactivated."]
        
        amount = Decimal(amount)
        
        # Check if overdraft is needed
        if amount > customer['balance_checking']:
            required_balance = amount + 35  # Overdraft fee included
            new_balance = customer['balance_checking'] - required_balance  # Potential new balance
            
            print(f"Required balance: {required_balance}")
            print(f"Current balance: {customer['balance_checking']}")
            print(f"New balance if withdrawn: {new_balance}")
            
            # If the new balance would be below -100, deny the transaction
            if new_balance < -135:
                return [False, "Insufficient balance after overdraft fee is applied, transaction cancelled."]
            
            # Otherwise, apply overdraft fee and withdraw
            customer['balance_checking'] -=35
            customer['overdraft_count'] += 1

            if customer['overdraft_count'] > 2:
                return [False, "Account deactivated due to excessive overdrafts."]
            
            return [True, f"Overdraft fee applied. New balance: {customer['balance_checking']}, Overdraft count: {customer['overdraft_count']}. Max allowed overdrafts: 2."]
        
        # If no overdraft is needed, proceed with normal withdrawal
        # customer['balance_checking'] -= amount
        return [True, "Withdraw allowed."]


    # def can_withdraw(self, customer, amount):
    #     if customer["active"] == False:
    #         return [False, "Account is deactivated."]

    #     amount = Decimal(amount)

    #     if amount > customer['balance_checking']:
    #         if customer['balance_checking'] >= Decimal('-100.00'):
    #             if Decimal(amount) > customer['balance_checking']:
    #                 print("Overdraft occurred. A fee of $35 will be charged.")
    #                 customer['balance_checking'] -= Decimal(amount)
    #                 customer['balance_checking'] -= Decimal('35.00')
    #                 print(f"$35 fee applied. New balance is: {customer['balance_checking']}")
    #                 customer['overdraft_count'] += 1

    #                 if customer['overdraft_count'] > 2:
    #                     print("Too many overdrafts. The account will be deactivated.")
    #                     customer['active'] = False
    #                     return [False, "Account deactivated due to excessive overdrafts."]
    #                 return [False, "Insufficient balance after overdraft fee."]
    #             return [False, "Insufficient balance."]
    #         return [False, "Insufficient balance."]

    #     return [True, "Withdraw allowed."]

    def withdraw(self, customer, amount, bank):
        [can_withdraw, message] = self.can_withdraw(customer, amount)
        if can_withdraw :
            customer['balance_checking'] -= Decimal(amount)
            print(f"Withdrawn {amount}. New balance is: {customer['balance_checking']}")

            for c in bank.customers:
                if c['a_id'] == customer['a_id']:
                    c['balance_checking'] = customer['balance_checking']

            bank.write_csv()
        else:
            print(message)


class Saving_account:
    def __init__(self):
        self.balance = Decimal('0.00')

    def deposit(self, customer, amount, bank):
        amount = Decimal(amount)
        customer['balance_saving'] += amount
        print(f"Deposited {amount}. New balance is: {customer['balance_saving']}")

        if customer['balance_saving'] >= 0 and customer['active'] == False:
            print("Account has been reactivated as the balance is now positive.")
            customer['active'] = True  # Reactivate account

        for c in bank.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_saving'] = customer['balance_saving']
        bank.write_csv()

    def can_withdraw(self, customer, amount):
        if customer["active"] == False:
            return [False, "Account is deactivated."]

        amount = Decimal(amount)

        if amount > customer['balance_saving']:
            if customer['balance_checking'] >= Decimal('-100.00'):
                print("Overdraft occurred. A fee of $35 will be charged.")
                customer['balance_checking'] -= Decimal('35.00')
                print(f"$35 fee applied. New balance is: {customer['balance_checking']}")
                customer['overdraft_count'] += 1

            return [False, "Insufficient balance in savings."]

            if customer['overdraft_count'] > 2:
                customer['active'] = False
                return [False, "Too many overdrafts. Account deactivated."]
            
            return [True, "Withdraw allowed, with overdraft fee applied."]

        return [True, "You can withdraw without overdraft."]

    def withdraw(self, customer, amount, bank):
        [can_withdraw, message] = self.can_withdraw(customer, amount)
        if can_withdraw:
            customer['balance_saving'] -= Decimal(amount)
            print(f"Withdrawn {amount}. new balance is: {customer['balance_checking']}")
            for c in bank.customers:
                if c['a_id'] == customer['a_id']:
                   c['balance_checking'] = customer['balance_checking']
            bank.write_csv()
        else:
            print(message)

def main():
    bank = Bank()
    bank.load_data()
    logged_in_customer = None
    while True:
        print("\n--- Welcome to the Python Bank ---")
        print("1. New Customer")
        print("2. Login to Account")
        print("3. Exit")
        print("-------------------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            option = input("What type of account do you want: 1) Checking account  2) Saving account  3) Both: ")

            Fname_input = str(input("Enter customer's first_name: "))
            Lname_input = str(input("Enter customer's last_name: "))
            password_input = input("Enter customer's password: ")
            balance_checking_input = ""
            balance_saving_input = ""
            account_type = ""
            active = True
            overdraft_count = 0

            if option == '1':
                balance_checking_input = 0

            if option == '2':
                balance_saving_input = 0

            if option == '3':
                balance_checking_input = 0
                balance_saving_input = 0

            customer_instance = Customer(Fname_input, Lname_input, password_input, balance_checking_input, balance_saving_input, active, overdraft_count)
            bank.add_customer(customer_instance)
        
        elif choice == '2':
            logged_in_customer = bank.login()
            print(logged_in_customer)
            if logged_in_customer:
                while True:
                    print("\n--- Account Operations ---")
                    print("1. Deposit Money into Checking Account")
                    print("2. Deposit Money into Saving Account")
                    print("3. Withdraw Money from Checking Account")
                    print("4. Withdraw Money from Saving Account")
                    print("5. Check Balance of Checking Account")
                    print("6. Check Balance of Saving Account")
                    print("7. transfer from checking account to saving")
                    print("8. transfer from saving account to checking")
                    print("9. transfer from account to account")
                    print("10. Display all information ")
                    print("11. Logout")

                    choice = input("Enter your choice: ")
                    checking = Checking_account()
                    saving = Saving_account()

                    if choice == '1':
                        amount = 0
                        while type(amount) != 'float' and amount < 1.00:
                            amount = input("Enter amount to deposit into checking: ")
                            try:
                                amount = float(amount)
                            except ValueError:
                                print("please enter a real number")

                        logged_in_customer['balance_checking'] = 0 if logged_in_customer['balance_checking'] == None else logged_in_customer['balance_checking'] 
                        checking.deposit(logged_in_customer, amount, bank)

                    elif choice == '2':
                        amount = 0
                        while type(amount) != 'float' and amount < 1.00:
                            amount = input("Enter amount to deposit into saving: ")
                            try:
                                amount = float(amount)
                            except ValueError:
                                print("please enter a real number")

                        logged_in_customer['balance_saving'] = 0 if logged_in_customer['balance_saving'] == None else logged_in_customer['balance_saving'] 
                        saving.deposit(logged_in_customer, amount, bank)

                    elif choice == '3':
                        amount = 0
                        while type(amount) != 'float' and amount < 1.00:
                            amount = input("Enter amount to withdraw from checking: ")
                            amount = Decimal(amount) 
                            try:
                                amount = float(amount)
                            except ValueError:
                                print("please enter a real number")

                        logged_in_customer['balance_checking'] = 0 if logged_in_customer['balance_checking'] == None else logged_in_customer['balance_checking'] 
                        checking.withdraw(logged_in_customer, amount, bank)

                    elif choice == '4':
                        amount = 0
                        while type(amount) != 'float' and amount < 1.00:
                            amount = input("Enter amount to withdraw from saving: ")
                            try:
                                amount = float(amount)
                            except ValueError:
                                print("please enter a real number")

                        logged_in_customer['balance_checking'] = 0 if logged_in_customer['balance_checking'] == None else logged_in_customer['balance_checking'] 
                        saving.withdraw(logged_in_customer, amount, bank)


                    elif choice == '5':
                        print(f"Checking Balance: {logged_in_customer['balance_checking']}")

                    elif choice == '6':
                        print(f"Savings Balance: {logged_in_customer['balance_saving']}")

                    elif choice == '7':
                        amount = 0
                        while type(amount) != 'float' and amount < 1.00:
                            amount = input("Enter amount to transfer from checking to saving: ")
                            try:
                                amount = float(amount)
                            except ValueError:
                                print("please enter a real number")

                        logged_in_customer['balance_saving'] = 0 if logged_in_customer['balance_saving'] == None else logged_in_customer['balance_saving'] 
                        bank.transfer_from_checking_to_saving(logged_in_customer, amount)
                        # amount = None
                        # while type(amount) != 'float' or amount < 1: 
                        #     amount = input("Enter amount to transfer from checking to saving: ")
                        # bank.transfer_from_checking_to_saving(logged_in_customer, amount) 

                    elif choice == '8':
                        amount = 0
                        while type(amount) != 'float' and amount < 1.00:
                            amount = input("Enter amount to transfer from saving to checking: ")
                            try:
                                amount = float(amount)
                            except ValueError:
                                print("please enter a real number")

                        logged_in_customer['balance_checking'] = 0 if logged_in_customer['balance_checking'] == None else logged_in_customer['balance_checking'] 
                        bank.transfer_from_saving_to_checking(logged_in_customer, amount)

                    elif choice == '9':
                        recipient_id = input("Enter the recipient's account ID: ")
                        amount = float(input("Enter the amount to transfer: "))

                        recipient = None
                        # Find the recipient by account ID
                        for c in bank.customers:
                            if str(c['a_id']) == recipient_id:
                                recipient = c
                                break

                        if recipient:
                            # Perform the transfer
                            bank.transfer_from_account_to_account(logged_in_customer, recipient, amount)
                        else:
                            print("Recipient not found.")

                    elif choice == '10':
                        print(f"Account Information for {logged_in_customer['first_name']} {logged_in_customer['last_name']}")
                        print(f"Account ID: {logged_in_customer['a_id']}")
                        print(f"Checking Balance: {logged_in_customer['balance_checking']}")
                        print(f"Savings Balance: {logged_in_customer['balance_saving']}")
                    elif choice == '11':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Try again.") 
        elif choice == '3':
            print("Thank you for using Python Bank!")
            break   
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()    