import random
import csv
import os

global global_id 
global_id = 10001

class Bank:
    def __init(self, customers = None ):
        if customers is None:
            customers = []
        self.customers = customers
        self.fieldnames = ["a_id", "first_name", "last_name", "password" , "balance_checking" , "balance_saving"]

    customers = [
        { 'a_id': 1, 'first_name': 'suresh', 'last_name': 'sigera', 'password': '1', 'balance_checking': None, 'balance_saving': 10000 },
        { 'a_id': 2 ,'first_name': 'james'  , 'last_name': 'taylor' , 'password': '2'  , 'balance_checking': 0 , 'balance_saving': 0  }, 
        { 'a_id': 10003 ,'first_name': 'melvin' , 'last_name': 'gordon' , 'password': 'uYWE732g4ga1' , 'balance_checking': 2000  , 'balance_saving': 20000  }, 
        { 'a_id': 10004 ,'first_name': 'stacey' , 'last_name': 'abrams' , 'password': 'DEU8_qw3y72$' , 'balance_checking': 2000  , 'balance_saving': 20000  }, 
        { 'a_id': 10005 ,'first_name': 'jake'   , 'last_name': 'paul'   , 'password': 'd^dg23g)@'    , 'balance_checking': 100000, 'balance_saving': 100000 }
    ]  

    fieldnames = ["a_id", "first_name", "last_name", "password" , "balance_checking" , "balance_saving"]
    
    def write_csv(self):
        global global_id
        if not os.path.exists("./bank.csv"):
            with open("./bank.csv", 'w', newline='') as csvfile:
                try:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                    writer.writeheader()
                    for row in self.customers:
                        writer.writerow(row)
                        # print(global_id, "checking global 34")
                        if int(row["a_id"]) > global_id:
                            global_id = row["a_id"]
                except csv.Error as e:
                    print(e)
        else:
            with open("./bank.csv", 'w', newline='') as csvfile:
                try:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                    writer.writeheader()
                    for row in self.customers:
                        writer.writerow(row)
                        # print(row["a_id"], global_id, "checking global 34")
                        if row["a_id"] >= global_id:
                            global_id = row["a_id"]
                            # writer.writerow(row)
                except csv.Error as e:
                    print(e)
   

    def add_customer(self , customer):
        self.customers.append({ 
            'a_id': customer.a_id, 
            'first_name': customer.first_name, 
            'last_name': customer.last_name, 
            'password': customer.password, 
            'balance_checking': customer.balance_checking, 
            'balance_saving': customer.balance_saving 
            })
        self.write_csv()
        #Use add new row here with the new customer data?
        print(f"Account for {customer.first_name} {customer.last_name} added successfully!")

    def login(self): 
        with open("bank.csv", mode='r',  encoding='utf-8', newline='') as file:
            userreader = csv.reader(file, delimiter=',')
            a_id = input("Your registered Account ID? ")
            c_pw = input("Your password? ")
            for row in userreader:
                reg_id = row[0]
                reg_pass = row[3]
                if a_id == reg_id and c_pw == reg_pass:
                    print(f"Hey, {row[1]}! Welcome back.")
                    return row
            print("The login details are not valid.")

    def transfer_from_checking_to_saving(self, customer, amount):
        checking_account = Checking_account(customer, customer[4])
        saving_account = Saving_account(customer, customer[5])

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if checking_account.get_balance() < amount:
            print("Insufficient balance in savings account.")
            return

        checking_account.balance -= amount
        saving_account.balance += amount
        customer[4] = checking_account.balance
        customer[5] = saving_account.balance

        print(f"Successfully transferred {amount} from chacking to saving.")
        print(f"New Checking Account Balance: {checking_account.balance}")
        print(f"New Savings Account Balance: {saving_account.balance}")

    def transfer_from_savings_to_checking(self, customer, amount):
        checking_account = Checking_account(customer, customer[4])
        saving_account = Saving_account(customer, customer[5])

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if saving_account.get_balance() < amount:
            print("Insufficient balance in savings account.")
            return

        saving_account.balance -= amount
        checking_account.balance += amount
        customer[4] = checking_account.balance
        customer[5] = saving_account.balance

        print(f"Successfully transferred {amount} from savings to checking.")
        print(f"New Checking Account Balance: {checking_account.balance}")
        print(f"New Savings Account Balance: {saving_account.balance}")    

       
class Customer(Bank):

    def __init__(self, first_name, last_name, password, balance_checking =0 , balance_saving = 0):

        global global_id
        global_id += 1
        self.a_id = global_id
        self.first_name= first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_saving = balance_saving

    def display_customer_fieldnames(self):
        print("customer fieldnames: a_id, first_name, last_name, password, balance_checking, balance_saving")

    def display_customer(self, customer):  
        print(f"ID of Account: {customer['a_id']}.")
        print(f"First Name of Customer: {customer['first_name']}")
        print(f"Last Name of Customer: {customer['last_name']}")
        print(f"Checking Balance of Customer: {customer['balance_checking']}")
        print(f"Savings Balance of Customer: {customer['balance_saving']}") 


class Checking_account :

    def __init__(self, customer , balance ):
        self.customer= customer
        self.balance = float(balance)
        self.activated_account = True  # Assume account is activated
        self.count_of_overdraft = 0 

    def deposit(self , amount):
        # print(self.balance)
        # print(amount)
        if amount > 0:
            self.balance += amount  # f"{int(self.balance)+int(amount)}"
            self.customer[4] = self.balance 
            print(f"deposited {amount}. new balance is: {self.balance}")
        else :
            print("deposited amount must be positive") 

    def withdraw(self, amount):
        self.account_access()
        if amount > self.balance:
            if self.balance <= 0:
                print("The amount you are allowed to transfer must not exceed $100 - a fine of $35 will be imposed.")
                if amount <= 100:
                   self.balance -= amount
                   self.balance -= 35  
                   self.customer[5] = self.balance
                   print(f"{amount} withdrawn successfully..  new balance is: {self.balance}")
                else:
                    print("Withdrawals of more than $100 are not allowed.")   
            else:
                print("Insufficient balance.")

        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount # f"{int(self.balance)-int(amount)}"
            self.customer[5] = self.balance 
        print(f"{amount} withdrawn successfully..  new balance is: {self.balance}")

    def account_access(self):
        if not self.activated_account:
            print("The account is deactivated. No transactions allowed.")
            return False  # Prevent further transactions if the account is deactivated
        return True

    def track_overdraft(self):
        if self.balance < 0:
            self.count_of_overdraft += 1
            if self.count_of_overdraft > 2:
                self.activated_account = False
                print("The account has been deactivated due to excessive overdrafts.")


    # def withdraw(self, amount):
    #     if amount > self.balance: #int(self.balance):
    #         print("Insufficient balance.")
    #     elif amount <= 0:
    #         print("Withdrawal amount must be positive.")
    #     else:
    #         self.balance -= amount # f"{int(self.balance)-int(amount)}"
    #         self.customer[4] = self.balance 
    #     print(f"{amount} withdrawn successfully..  new balance is: {self.balance}")       

    def get_balance(self):
      return self.balance

    # def display(self):
    #     print ("checking Account")
    #     print(f"Account ID: {self.a_id}")
    #     print(f"Account Holder: {self.first_name} {self.last_name}")
    #     print(f"Balance: {self.balance_checking}")

    def display(self):
        print("Checking Account")
        print(f"Account ID: {self.customer['a_id']}")
        print(f"Account Holder: {self.customer['first_name']} {self.customer['last_name']}")
        print(f"Balance: {self.balance}")
     


class Saving_account:

    def __init__(self, customer , balance ):
        self.customer= customer
        self.balance = float(balance)
        self.activated_account = True  
        self.count_of_overdraft = 0 

    def deposit(self , amount):
        print(self.balance)
        print(amount)
        if amount > 0:
            self.balance += amount  # f"{int(self.balance)+int(amount)}"
            self.customer[5] = self.balance 
            print(f"deposited {amount}. new balance is: {self.balance}")
        else :
            print("deposited amount must be positive")



    # def withdraw(self, amount):
    #     if amount > self.balance:

    #         print("Insufficient balance.")
    #     elif amount <= 0:
    #         print("Withdrawal amount must be positive.")
    #     else:
    #         self.balance -= amount # f"{int(self.balance)-int(amount)}"
    #         self.customer[5] = self.balance 
    #     print(f"{amount} withdrawn successfully..  new balance is: {self.balance}") 

    def withdraw(self, amount):
        self.account_access()
        if amount > self.balance:
            if self.balance <= 0:
                print("The amount you are allowed to transfer must not exceed $100 - a fine of $35 will be imposed.")
                if amount <= 100:
                    self.balance -= amount
                    self.balance -= 35  
                    self.customer[5] = self.balance
                    print(f"{amount} withdrawn successfully..  new balance is: {self.balance}")
                else:
                    print("Withdrawals of more than $100 are not allowed.")
            else:
                print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.customer[5] = self.balance
            print(f"{amount} withdrawn successfully..  new balance is: {self.balance}")

    def account_access(self):
        if not self.activated_account:
            print("The account is deactivated. No transactions allowed.")
            return False  
        return True

    def track_overdraft(self):
        if self.balance < 0:
            self.count_of_overdraft += 1
            if self.count_of_overdraft > 2:
                self.activated_account = False
                print("The account has been deactivated due to excessive overdrafts.")
      

    def get_balance(self):
      return self.balance

    def display(self):
        print ("Saving Account")
        print(f"Account ID: {self.a_id}")
        print(f"Account Holder: {self.first_name} {self.last_name}")
        print(f"Balance: {self.balance_saving}")

def main():
    bank = Bank()
    bank.write_csv()
    logged_in_customer = []
    while True:
        print("\n--- Welcome to the Python Bank ---")
        print("1. New Customer")
        print("2. Login to Account")
        print("3. Exit")
        print("-------------------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            option = input("What type of account do you want: 1) Checking account  2) Saving account  3) Both: ")

            Fname_input = input("Enter customer's first_name: ")
            Lname_input = input("Enter customer's last_name: ")
            password_input = input("Enter customer's password: ")
            balance_checking_input = None
            balance_saving_input = None
            account_type = None

            if option == '1':
                balance_checking_input = 0

            if option == '2':
                balance_saving_input = 0

            if option == '3':
                balance_checking_input = 0
                balance_saving_input = 0

            customer_instance = Customer(Fname_input, Lname_input, password_input, balance_checking_input, balance_saving_input)
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
                    print("9. Display all information ")
                    print("10. Logout")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        amount = float(input("Enter amount to deposit into checking: "))
                        print(logged_in_customer[4])
                        checking_account = Checking_account(logged_in_customer, logged_in_customer[4])
                        checking_account.deposit(amount)

                    elif choice == '2':
                        amount = float(input("Enter amount to deposit into saving: "))
                        saving_account = Saving_account(logged_in_customer, logged_in_customer[5])
                        saving_account.deposit(amount)

                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw from checking: "))
                        checking_account = Checking_account(logged_in_customer, logged_in_customer[4])
                        checking_account.withdraw(amount)

                    elif choice == '4':
                        amount = float(input("Enter amount to withdraw from saving: "))
                        saving_account = Saving_account(logged_in_customer, logged_in_customer[5])
                        saving_account.withdraw(amount)

                    elif choice == '5':
                        checking_account = Checking_account(logged_in_customer, logged_in_customer[4])
                        print(f"Checking Balance: {checking_account.balance}")

                    elif choice == '6':
                        saving_account = Saving_account(logged_in_customer, logged_in_customer[5])
                        print(f"Savings Balance: {saving_account.balance}")

                    elif choice == '7':
                        amount = float(input("Enter amount to transfer from checking to saving: "))
                        bank.transfer_from_checking_to_saving(logged_in_customer, amount) 

                    elif choice == '8':
                        amount = float(input("Enter amount to transfer from savings to checking: "))
                        bank.transfer_from_savings_to_checking(logged_in_customer, amount)   

                    elif choice == '9':
                        print(f"Account Information for {logged_in_customer[1]} {logged_in_customer[2]}")
                        print(f"Account ID: {logged_in_customer[0]}")
                        print(f"Checking Balance: {logged_in_customer[4]}")
                        print(f"Savings Balance: {logged_in_customer[5]}")

                    elif choice == '10':
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

# ---------------------------------------------------------------------
