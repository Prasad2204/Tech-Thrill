# Dictionary
menu = {
    'Daal Rice': 50,
    'Chaapati Bhaji': 60,
    'Veg Tiffin': 100,
    'Non-Veg Tiffin': 140,
    'Bhakari Chicken': 80,
}

print("WELCOME TO MADEBYMOM")
print('\nThis is our Menu:')

print("Daal Rice:50Rs\nChaapati Bhaji:60Rs\nVeg Tiffin:100Rs\nNon-Veg Tiffin:140Rs\nBhakari Chicken:80Rs")
order_total = 0
item_1 = input("Enter the name of item you want to order :")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available.\n Please order something that is available.")
flag = True
while flag:
    another_order = input("Do you want to ordered another item? (yes/no):")
    if another_order == "yes":
        item_2 = input("Enter the name of the next item :")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} is added to order.")
        else:
            print(f"Ordered item {item_1} is not available.\n Please order something that is available.")
    else:
        flag = False
print(f"\nThank You for your order.")
print(f"The Total amount to pay for order is {order_total}")

