# ![](https://www.tripwire.com/sites/default/files/Untitled-design5-5.jpg) Python Banking


## Description

This program a fun and interactive banking simulation program that allows users to manage their accounts, perform deposits and withdrawals, and transfer money between checking and savings accounts. 🏦💸
The system stores customer data in a CSV file (bank.csv), and allows account operations such as logging in, transferring funds between accounts, overdraft management, and account reactivation.💰

## Technologies Used 

- Python: The heart and soul of the system! 
- CSV 📊: For storing and handling customer data.
- Decimal: For handling monetary transactions with precision.
- OOP (Object-Oriented Programming): Using classes and objects to make everything neat and organized.

## App Functionality / User Stories

**Account Management**

- Add Customer: Create new customer accounts with unique Account IDs (auto-generated).
- Login: Customers can log in using their account ID and password.
- Display Customer Info: Show customer account details, such as checking and savings balance.

**Account Operations**

- Deposit: Make deposits into checking or savings accounts.
- Withdraw: Withdraw from checking or savings accounts. If the account balance is insufficient, an overdraft fee is applied.
- Transfer: Transfer money between checking and savings accounts or between different customers' checking accounts.

**Overdraft Management**

- Overdraft Count: If a customer withdraws more than their balance, an overdraft fee of $35 is applied. After 2 overdrafts, the account will be deactivated.

**Reactivate Accounts**

- Reactivation: Accounts that are deactivated due to overdrafts can be reactivated if a deposit brings the account balance back to positive.

## Files and Structure

- **bank.csv**: This is where customer data is stored (account ID, first name, last name, password, checking balance, saving balance, overdraft count, and account status).

- **banking.py**: This is the main Python script that handles customer and account operations.

## Classes Overview
### 1. `Bank`

This class is responsible for managing customers and handling various banking operations.
- **Methods**: 
    - `laod_data()`: Loads customer data from the CSV file.
    - `write_csv()`: Saves updated customer data back to the CSV file.
    - `add_customer()`: Adds a new customer.
    - `login()`: Validates customer login details.
    - `transfer_from_checking_to_saving()`: Transfers money from checking to savings account.
    - `transfer_from_saving_to_checking()`: Transfers money from savings to checking account.
    -`transfer_from_account_to_account()`: Transfers money between two customer accounts.

### 2. ` Customer` (Subclass of `Bank`)

Represents an individual customer and contains their personal information, account balances, and methods to display details.

- **Methods**: 
    - `display_customer_fieldnames()`: Displays the list of customer fieldnames.

### 3. `Checking_account`

Handles checking account operations like deposits, withdrawals, and overdraft management.

- **Methods**: 
    - `deposit()`: Makes a deposit into the checking account.
    - `can_withdraw()`: Checks if a withdrawal is allowed considering overdraft fees and account balance.
    - `withdraw()`: Withdraws money from the checking account.

### 4. `Saving_account`

Handles savings account operations like deposits, withdrawals, and overdraft management.

- **Methods**: 
    - `deposit()`: Makes a deposit into the savings account.
    - `can_withdraw()`: Checks if a withdrawal is allowed considering overdraft fees and account balance.
    - `withdraw()`: Withdraws money from the savings account.

## CSV Data Structure

The customer data is stored in a CSV file (`bank.csv`) with the following fields:<br/>

| Field Nam            | Description |
|-----------------     |-------------|
| `a_id`               | Account ID (unique integer) |
| `first_name`         | Customer's first name |
| `last_name`          | Customer's last name|
| `password`           | Account password |
| `balance_checking`   | Checking account balance|
| `balance_saving`     | Savings account balance|
| `overdraft_count`    | Number of overdrafts applied | 
| `active`             |  Account status (True/False) |


## Icebox Features

Imagine adding these cool features in the future:

- 🔒 Password Encryption: Add security to passwords by encrypting them.
- 🌐 Web Interface: A web app version could make banking even more interactive.
- 📱 Mobile App: A Mopile app version could make banking even more easer and interactive.
- 💳 Payment Integration: Link accounts with external services for a real experience. Think of it as your own virtual ATM! 🏧
- 🎯 Personalized Offers: Provide customers with targeted deals, like a savings plan or low-interest loans. 💡

## Challenges / Key Takeaways 
### Challenges:
1. Overdraft Logic: Handling overdrafts and applying the right fees can be tricky, especially with multiple account states to consider. Managing balance checks and deciding when to deactivate accounts added some complexity.
2. Data Management: Storing customer data in a CSV file instead of a more secure database makes the project simpler, but also more prone to concurrency issues and potential data loss. It's a reminder that in real-world banking, data security and storage are critical! 🔐
3. User Interface: The lack of a GUI made it challenging to provide real-time feedback and a smoother user experience. CLI (command-line interface) is fun but can be limiting for more complex systems. 

### Key Takeaways:
1. Mastering CSVs: Reading and writing to CSV files was an essential part of this project. It taught me how to persist data without a full-fledged database system. 🧑‍💻
2. Real-World Banking Concepts: Implementing overdraft protection, transaction logging, and account management mimicked real banking workflows. I now have a deeper appreciation for the complexities of even the most basic banking systems. 💡
3. Object-Oriented Design: This project helped me sharpen my skills in OOP by creating well-defined classes and methods, helping me think in terms of objects and relationships. 




