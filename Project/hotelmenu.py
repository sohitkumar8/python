#Define the menu of restaurant
menu = {
    "Pizza":60,
    "Pasta":50,
    "Maggie":90,
    "Burger":40,
    "Coffee":70
}
#Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs60\nPasta: Rs50\nMaggie: Rs90\nBurger: Rs40\nCoffee: Rs70")

order_total = 0
# 50+90=140

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Order item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Order item {item_2} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")