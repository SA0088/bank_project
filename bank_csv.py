# Python's CSV package will give you all you need to Create, Read, Update, Delete a CSV.
# This functionality is all you will need to be able to complete your Python Banking Project.
# The official docs are accessible here: https://docs.python.org/3/library/csv.html#

# HINT:
# Using a dictionary is a good data structure to translate into a CSV, because:
# * A list of dictionaries is similar to rows in a table
# * Each key in a dictionary can correspond to a column name

# HOW TO USE:
# 1.0 Import the csv and os packages:
import csv
import os

# 1.1 Seed Data to CSV
customer_who_info = [
    { 'ID': 10001 ,'First name': 'suresh' , 'Last name': 'sigera' , 'Passsword': 'juagw362'     , 'balance_checking': 1000  , 'balance_saving': 10000  },
    { 'ID': 10002 ,'First name': 'james'  , 'Last name': 'taylor' , 'Passsword': 'idh36%@#FGd'  , 'balance_checking': 10000 , 'balance_saving': 10000  }, 
    { 'ID': 10003 ,'First name': 'melvin' , 'Last name': 'gordon' , 'Passsword': 'uYWE732g4ga1' , 'balance_checking': 2000  , 'balance_saving': 20000  }, 
    { 'ID': 10004 ,'First name': 'stacey' , 'Last name': 'abrams' , 'Passsword': 'DEU8_qw3y72$' , 'balance_checking': 2000  , 'balance_saving': 20000  }, 
    { 'ID': 10005 ,'First name': 'jake'   , 'Last name': 'paul'   , 'Passsword': 'd^dg23g)@'    , 'balance_checking': 100000, 'balance_saving': 100000 }
]

# 2.0 Set fieldnames once:
fieldnames = ["ID", "First name", "Last name", "password" , "balance_checking" , "balance_saving"]

# 3.0 Check CSV File Exists (otherwise error thrown!)
# 3.1 Set Headers in the CSVFile 
# 3.2 SEED DATA TO CSV
# 3.3 EXAMPLE: writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# 3.4 "w" option will allow writing, but NOT appending...
if not os.path.exists("./bank.csv"):
    with open("./bank.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customer_who_info:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

# 4.0 If Exists - ReadFile / Rows:
try: 
    with open("bank.csv", "r") as file:
        contents = csv.DictReader(file)
        for row in contents:
            print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Passsword': '134'}
            for prop in fieldnames:
                print(row[prop]) # will print the value of each individual property
except csv.Error as e:
    print(e)


# 5.0 Add Individual Row => "a+" option will allow reading and APPENDING to file
try:
    new_row = {'Name': 'The Sixth Doctor', 'Actor': 'Harrison Ford', 'Passsword': 1 }
    with open("doctor_who.csv", "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_row)
except csv.Error as e:
    print(e)


# 6.0 Updating A row
# --- There is no no way to directly update one single row using the Python CSV import module
# --- or through any other means you will have access to. This means you will have to work through 
# --- using data structures to find a way to update an individual item and rewrite the entire file.
# --- we will walk through this process in class.



# 7.0 Deleting A Row
# --- There is no no way to directly delete one single row using the Python CSV import module
# --- or through any other means you will have access to. This means you will have to work through 
# --- using data structures to find a way to delete an individual item and rewrite the entire file.
# --- we will walk through this process in class.