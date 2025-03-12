import random
import csv
import os

global global_id
global_id = 10001

customers = [
    { 'a_id': 10001, 'first_name': 'suresh', 'last_name': 'sigera', 'password': '1', 'balance_checking': None, 'balance_saving': 10000, 'overdraft_count': 0, "active": True },
    { 'a_id': 10002 ,'first_name': 'james'  , 'last_name': 'taylor' , 'password': '2'  , 'balance_checking': 0 , 'balance_saving': 0, 'overdraft_count': 0, "active": True  }, 
    { 'a_id': 10003 ,'first_name': 'melvin' , 'last_name': 'gordon' , 'password': 'uYWE732g4ga1' , 'balance_checking': 2000  , 'balance_saving': 20000, 'overdraft_count': 0, "active": True }, 
    { 'a_id': 10004 ,'first_name': 'stacey' , 'last_name': 'abrams' , 'password': 'DEU8_qw3y72$' , 'balance_checking': 2000  , 'balance_saving': 20000, 'overdraft_count': 0, "active": True }, 
    { 'a_id': 10005 ,'first_name': 'jake'   , 'last_name': 'paul'   , 'password': 'd^dg23g)@'    , 'balance_checking': 100000, 'balance_saving': 100000, 'overdraft_count': 0, "active": True }
]

fieldnames = ["a_id", "first_name", "last_name", "password" , "balance_checking" , "balance_saving", "overdraft_count", "active"]

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
                    row['overdraft_count'] = int(row['overdraft_count']) if type(row['overdraft_count']) == 'int' else 0
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
            'overdraft_count': customer.overdraft_count,
            'active': customer.active
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
        return None

    def transfer_from_checking_to_saving(self, customer, amount):
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

    def transfer_from_saving_to_checking(self, customer, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if customer['balance_saving'] < amount:
            print("Insufficient balance in savings account.")
            return

        customer['balance_checking'] += amount
        customer['balance_saving'] -= amount

        print(f"Successfully transferred {amount} from savings to checking.")
        print(f"New Checking Account Balance: {customer['balance_checking']}")
        print(f"New Savings Account Balance: {customer['balance_saving']}")

class Customer(Bank):
    def __init__(self, first_name, last_name, password, balance_checking, balance_saving, active, overdraft_count):
        global global_id
        global_id += 1
        self.a_id = global_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_saving = balance_saving
        self.active = active
        self.overdraft_count = overdraft_count

    def display_customer_fieldnames(self):
        print("Customer fieldnames: a_id, first_name, last_name, password, balance_checking, balance_saving, overdraft_count, active")

    def display_customer(self, customer):  
        print(f"ID of Account: {customer['a_id']}.")
        print(f"First Name of Customer: {customer['first_name']}")
        print(f"Last Name of Customer: {customer['last_name']}")
        print(f"Checking Balance of Customer: {customer['balance_checking']}")
        print(f"Savings Balance of Customer: {customer['balance_saving']}")

class Checking_account:

    def __init__(self):
        pass

    def deposit(self, customer, amount, bank):
        customer['balance_checking'] += amount
        print(f"Deposited {amount}. New balance is: {customer['balance_checking']}")
        for c in bank.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_checking'] = customer['balance_checking']
        bank.write_csv()

    def withdraw(self, customer, amount, bank):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if customer['balance_checking'] < amount:
            print("Insufficient balance.")
            return

        customer['balance_checking'] -= amount
        print(f"Withdrawn {amount}. New balance is: {customer['balance_checking']}")
        for c in bank.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_checking'] = customer['balance_checking']
        bank.write_csv()

class Saving_account:

    def __init__(self):
        pass

    def deposit(self, customer, amount, bank):
        customer['balance_saving'] += amount
        print(f"Deposited {amount}. New balance is: {customer['balance_saving']}")
        for c in bank.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_saving'] = customer['balance_saving']
        bank.write_csv()

    def withdraw(self, customer, amount, bank):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if customer['balance_saving'] < amount:
            print("Insufficient balance.")
            return

        customer['balance_saving'] -= amount
        print(f"Withdrawn {amount}. New balance is: {customer['balance_saving']}")
        for c in bank.customers:
            if c['a_id'] == customer['a_id']:
                c['balance_saving'] = customer['balance_saving']
        bank.write_csv()

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
            Fname_input = input("Enter customer's first name: ")
            Lname_input = input("Enter customer's last name: ")
            password_input = input("Enter customer's password: ")
            balance_checking_input = 0
            balance_saving_input = 0
            active = True
            overdraft_count = 0

            customer_instance = Customer(Fname_input, Lname_input, password_input, balance_checking_input, balance_saving_input, active, overdraft_count)
            bank.add_customer(customer_instance)

        elif choice == '2':
            logged_in_customer = bank.login()
            if logged_in_customer:
                while True:
                    print("\n--- Account Operations ---")
                    print("1. Deposit Money into Checking Account")
                    print("2. Deposit Money into Saving Account")
                    print("3. Withdraw Money from Checking Account")
                    print("4. Withdraw Money from Saving Account")
                    print("5. Check Balance of Checking Account")
                    print("6. Check Balance of Saving Account")
                    print("7. Transfer from Checking Account to Saving")
                    print("8. Transfer from Saving Account to Checking")
                    print("9. Display all information")
                    print("10. Logout")

                    choice = input("Enter your choice: ")
                    checking = Checking_account()
                    saving = Saving_account()

                    if choice == '1':
                        amount = float(input("Enter amount to deposit into checking: "))
                        checking.deposit(logged_in_customer, amount, bank)

                    elif choice == '2':
                        amount = float(input("Enter amount to deposit into saving: "))
                        saving.deposit(logged_in_customer, amount, bank)

                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw from checking: "))
                        checking.withdraw(logged_in_customer, amount, bank)

                    elif choice == '4':
                        amount = float(input("Enter amount to withdraw from saving: "))
                        saving.withdraw(logged_in_customer, amount, bank)

                    elif choice == '5':
                        print(f"Checking Balance: {logged_in_customer['balance_checking']}")

                    elif choice == '6':
                        print(f"Savings Balance: {logged_in_customer['balance_saving']}")

                    elif choice == '7':
                        amount = float(input("Enter amount to transfer from checking to saving: "))
                        bank.transfer_from_checking_to_saving(logged_in_customer, amount)

                    elif choice == '8':
                        amount = float(input("Enter amount to transfer from saving to checking: "))
                        bank.transfer_from_saving_to_checking(logged_in_customer, amount)

                    elif choice == '9':
                        bank.display_customer(logged_in_customer)

                    elif choice == '10':
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice, please try again.")
        elif choice == '3':
            print("Thank you for using the Python Bank!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
