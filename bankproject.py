bank_accounts = {}

def create_account():
    acc_number = input("Enter account number: ")
    if acc_number in bank_accounts:
        print("Account already exists")
    else:
        name = input("Enter account holder name: ")
        bank_accounts[acc_number] = {"name": name, "balance": 0}
        print(f"Account created for {name} with account number {acc_number}")

def deposit():
    acc_number = input("Enter Account Number: ")
    if acc_number in bank_accounts:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            bank_accounts[acc_number]["balance"] += amount
            print(f"Deposited {amount}. Current Balance: {bank_accounts[acc_number]['balance']}")
        else:
            print("Invalid deposit amount")
    else:
        print("Account Not Found")

def withdraw():
    acc_number = input("Enter account number: ")
    if acc_number in bank_accounts:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= bank_accounts[acc_number]["balance"]:
            bank_accounts[acc_number]["balance"] -= amount
            print(f"Withdrawn {amount}. Remaining Balance: {bank_accounts[acc_number]['balance']}")
        else:
            print("Insufficient balance or invalid amount")
    else:
        print("Account Not Found")
        
def check_balance():
    acc_number = input("Enter account number: ")   
    if acc_number in bank_accounts:
        print(f"Account Holder: {bank_accounts[acc_number]['name']}")
        print(f"Current Balance: {bank_accounts[acc_number]['balance']}")
    else:
        print("Account Not Found")


def menu():
    while True:
        print("\n---Bank Menu---")
        print("1. Create Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. check balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
           create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
           check_balance()
        elif choice == '5':
            print("Thank you for using the Bank Application")
            break
        else:
            print("Invalid choice. Please try again.")
menu();
