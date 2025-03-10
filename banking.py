import random
import csv
import os

class Bank:
    def __init(self, customers = [], name = ""):
        if customers is None:
            customers = []
        self.customers = customers
        self.name = name

    def add_customer(self , customer):
        self.customers.append(customer)
        print("User added") 

    def display_customer(self):  
      print(f"ID of customer:  {customer_id} .")
      print(f"First name of customer:  {customer_Fname}")
      print(f"Last name of customer:  {customer_Lname}")

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

       
class Customer(Bank):

    def __init__(self, customer_id , customer_Fname , customer_Lname   , customer_password):
       self.customer_id = int(customer_id)
       self.customer_first_name= customer_First_name
       self.customer_last_name = customer_Last_name
       self.customer_password = customer_password
       self.account = None

    # @classmethod
    def add_account(self , account) :
        self.account = account



    def login_account(self):
        customer_id_login = input("Enter customer's ID: ")
        customer_pwd_login = input("Enter customer's password: ")
        if customer_id_login and customer_pwd_login in self.customers :
           print("login successfully")
        else:
           print("error") 

    def logout_account(self):
        exit()

class checking_account(Customer) :

    def __init__(self, customer_account_number , account_holder ,balance ):
        self.customer_account_number = generate_account_number
        self.account_holder = account_holder
        self.balance = 0

    def generate_account_number(self):
        return random.randint(10000,99999)

    def deposit(self , amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited {amount}. new balance is{self.balance}")
        else :
            print("deposited amount must be positive") 


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
        print(f"{amount} withdrawn successfully.")       

    def get_balance(self):
      return self.balance

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.customer_First_name} {self.customer_last_name}")
        print(f"Balance: {self.balance}")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print("Account not found.")
            return None   


class saving_account(Customer):

    def generate_account_number(self):
        return random.randint(10000,99999)

    def __init__(self, customer_account_number , account_holder ,balance ):
        self.customer_account_number = generate_account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposite(self , amount):
        if amount > 0:
            self.balance += amount
            print(f"deposited {amount}. new balance is{self.balance}")
        else :
            print("deposited amount must be positive") 


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
        print(f"{amount} withdrawn successfully.")       

    def get_balance(self):
      return self.balance

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.customer_First_name} {self.customer_Last_name}")
        print(f"Balance: {self.balance}")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print("Account not found.")
            return None    

def main():
    bank = Bank()
    while True:
        print("\n--- Welcome to the Python Bank ---")
        print("1. New Customer")
        print("2. Create Account")
        print("3. Login to Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Check Balance")
        # print("7. Display All Accounts")
        # print("8. Logout")
        # print("9. Exit")
      

        choice = input("Enter your choice: ")

            if choice == '1':
                customer_id_input = input("Enter customer's ID: ")
                customer_Fname_input = input("Enter customer's First name: ")
                customer_Lname_input = input("Enter customer's Last name: ")
                customer_password_input = input("Enter customer's password: ")
                customer_instance = Customer(customer_id_input, customer_Fname_input, customer_Lname_input,customer_password_input)
                Bank.add_customer(customer_instance)


    elif choice == '2':
        account_type_input = input ("What is account type you want: 1 fot checking account , 2 for saving account , 3 for both")
        if account_type_input == '1':
            account = checking_account()
            customer.add_account(account)
        elif account_type_input == '2':
            account = saving_account()
            customer.add_account(account)
        elif account_type_input == '3':
            account = checking_account() and saving_account()
            customer.add_account(account)
        else:
            print("please enter a valid number")
            return  



    elif choice == '3':
        customer_id_input = input("Enter your ID: ")
        customer_pwd_input = input ("Enter your password: ")
        if customer_id_input and customer_pwd_input in bank.customers:
            print("login successfully")
            return account
        else:
            print("invalid input")
        # account = checking_account.get_account(f"your checking account {account_number}") and saving_account.get_account (f"your saving account {account_number}")
        #     return account
 

    elif choice == '4':
        account
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            print(f"Account Balance: {account.get_balance()}")

    elif choice == '5':
        bank.display_all_accounts()
    elif choice == '6':
        print("Thank you for using Python Bank!")
        break   
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  
