
# Restaurant Management System

# Menu chart
menu = {
    'Pizza': 100,
    'Coffee': 80,
    'Pasta': 50,
    'Burger': 120,
    'Biriyani': 150
}

# Greeting
print("----- Welcome to Husen's Restaurant -----")

for item, price in menu.items():
    print(f"{item}: Rs {price}")

total_bill = 0

# First order
item_1 = input("Enter item: ").title()

if item_1 in menu:
    total_bill += menu[item_1]
    print("Your item added successfully!")
else:
    print(f"Item {item_1} is not available yet.")

# Second order
another_order = input(
    "Do you want any other dishes (yes/no): "
).lower()

if another_order == 'yes':
    item_2 = input("Enter second item: ").title()

    if item_2 in menu:
        total_bill += menu[item_2]
        print("Your item added successfully!")
    else:
        print(f"Item {item_2} is not available yet.")

# Final bill
print(f"Total bill is Rs {total_bill}")
