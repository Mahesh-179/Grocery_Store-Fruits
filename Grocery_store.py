
from datetime import datetime
from tabulate import tabulate

output=[]
balance=0
# FRUITS SECTION-Dictionary
menu_fruit={
    'apple': 350,
    'banana': 250,
    'orange': 200,
    'watermelon': 100,
    'grapes': 270,
}
# JUICE-SECTION-DICTIONARY
menu_juice={
    'apple': 200,
    'watermelon': 100,
    'mausami': 200,
    'sugarcane': 50,
    'coconut': 120,
}

# COLD DRINKS -DICTIONARY
menu_coldrinks={
    'coke': 70,
    'sprite':60,
    'fanta':50,
    'beer': 200,
    'whisky': 800,
}

# Display-fruit section
def display_fruit():
    table = [[item.capitalize(), price]
    for item, price in menu_fruit.items()]
    print(tabulate(table, headers=["Item", "Price (NPR)"], tablefmt="grid"))
    user = input("Enter your Items to purchase:- ")
    if user in menu_fruit:
        quantity1=int(input("Enter the quantity of " + user + ": "))
        total_price=quantity1*menu_fruit[user]
        output.append({
            'Item': user.capitalize(),
            'Quantity': quantity1,
            'Price': total_price,
            'timestamp': datetime.now()
        })
    print("\n Item purchased successfully.")

#display-juice section
def display_juice():
         table = [[item.capitalize(), price]
         for item, price in menu_juice.items()]
         print(tabulate(table, headers=["Item", "Price (NPR)"], tablefmt="grid"))
         user1 = input("Enter your Items to purchase:- ")
         if user1 in menu_juice:
             quantity2 = int(input("Enter the quantity of " + user1 + ": "))
             total_price = quantity2 * menu_juice[user1]
             output.append({
                 'Item': user1.capitalize(),
                 'Quantity': quantity2,
                 'Price': total_price,
                 'timestamp': datetime.now()
             })
         print("\n Item purchased successfully.")

def display_coldrink():
    table = [[item.capitalize(), price]
    for item, price in menu_coldrinks.items()]
    print(tabulate(table, headers=["Item", "Price (NPR)"], tablefmt="grid"))
    user2 = input("Enter your Items to purchase:- ")
    if user2 in menu_coldrinks:
        quantity3 = int(input("Enter the quantity of " + user2 + ": "))
        total_price = quantity3 * menu_coldrinks[user2]
        output.append({
            'Item': user2.capitalize(),
            'Quantity': quantity3,
            'Price': total_price,
            'timestamp': datetime.now()
        })
    print("\n Item purchased successfully.")

def display_1fruit():
    print("--------------- BILL --------------")
    rows = [[
        t['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
        t['Item'],
        t['Quantity'],
        t['Price'],

    ] for t in output]
    print(tabulate(rows, headers=["Time","Item", "Quantity","Price (NPR)"], tablefmt="grid"))

# Landing Main Interface
def main():
    while True:
        print("==================== MAHESH LAMSAL FRUIT SHOP ========================")
        print("1. Fruit")
        print("2. Juice")
        print("3. Coldrink")
        print("4. Bill & Payments")
        print("5. Exit")
        user_choice = int(input("Enter your choice:- "))
        if user_choice == 1:
            display_fruit()
        elif user_choice == 2:
            display_juice()
        elif user_choice == 3:
            display_coldrink()
        elif user_choice == 4:
            display_1fruit()
            print("Thank you for shopping!")
        elif user_choice == 5:
            print(" Thank you for Coming Here!")
            break
main()
