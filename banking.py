'''SVIST Bank of India - ATM Application
Overview
The SVIST Bank of India ATM application is a simple command-line interface (CLI) banking system that allows users
to create accounts, log in, view their balances, deposit, withdraw funds, and close their accounts.
The application uses MongoDB for data storage,
making it robust and capable of managing multiple user accounts securely.
->Create Account: Admin can create a new customer account with a unique customer ID, name, age, and address. The initial balance is set to 0.
->Login: Customers can log in using their name and customer ID.
->Show Balance: Customers can view their account balance.
->Deposit: Customers can deposit a specified amount into their account.
->Withdraw: Customers can withdraw a specified amount from their account if sufficient funds are available.
->Block/Delete Account: Customers can permanently delete their accounts.
->Exit: Customers can exit the application after performing an action.
'''
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["svist_bank"]
collection = db["customers"]

print("Welcome to SVIST Bank of India")

def add_customer():
    pas=input("ENTER ADMIN CODE TO CREATE ACCOUNT")
    if pas=="saireddy":
        customer_id = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        age = input("Enter customer age: ")
        address = input("Enter customer address: ")
        balance = 0.0  # Initialize balance to 0.0

        # Check if the customer already exists in MongoDB
        if collection.find_one({"$or": [{"customer_id": customer_id}, {"name": name}]}):
            print("Customer already exists. Try another way.")
            return

        # Insert the new customer into the collection
        customer = {
            "customer_id": customer_id,
            "name": name,
            "age": age,
            "address": address,
            "balance": balance
        }
        collection.insert_one(customer)
        print("Account created successfully")
        return
    else:
        print("invalid login")

def login():
    name = input("Enter your name: ")
    customer_id = input("Enter your ID: ")

    # Find the customer in MongoDB
    customer = collection.find_one({"name": name, "customer_id": customer_id})
    if customer:
        print("Login successful!")
        return customer
    else:
        print("Login failed :(")
    return None

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <= 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def update_balance(customer, new_balance):
    collection.update_one(
        {"customer_id": customer["customer_id"], "name": customer["name"]},
        {"$set": {"balance": new_balance}}
    )
    print("Balance updated successfully")

def delete_account(customer):
    result = collection.delete_one({"customer_id": customer["customer_id"], "name": customer["name"]})
    if result.deleted_count > 0:
        print("Account blocked (deleted) successfully!")
    else:
        print("Customer not found.")

def main(customer):
    balance = customer["balance"]
    is_running = True

    while is_running:
        print("******************")
        print("\n1. Show Balance")
        print("******************")
        print("2. Deposit")
        print("******************")
        print("3. Withdraw")
        print("******************")
        print("4. Block Account")
        print("******************")
        print("5. Exit")
        print("******************")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
            update_balance(customer, balance)
        elif choice == "3":
            balance -= withdraw(balance)
            update_balance(customer, balance)
        elif choice == "4":
            confirmation = input("Do you want to delete your account permanently? (Yes/No): ").lower()
            if confirmation == "yes":
                delete_account(customer)
                break
            elif confirmation == "no":
                continue
            else:
                print("Invalid option. Please choose Yes or No.")
        elif choice == "5":
            is_running = False
        else:
            print("Invalid option")

    print("Thank you! Have a nice day!")

# Start of the program
login_signup = input("1. Create account:\n2. Login account:\n")

if login_signup == "1":
    add_customer()
elif login_signup == "2":
    customer = login()
    if customer:
        main(customer)
else:
    print("Invalid choice.")
