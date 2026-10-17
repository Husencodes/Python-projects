
# Simple ATM Simulation

balance = 5000

def check_balance():
    print("Available Balance: Rs.", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance!")

while True:
    print("\n1. Balance  2. Deposit  3. Withdraw  4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1": check_balance()
    elif choice == "2": deposit()
    elif choice == "3": withdraw()
    elif choice == "4": break
    else: print("Invalid choice!")
print("Thank you for using our ATM!")
