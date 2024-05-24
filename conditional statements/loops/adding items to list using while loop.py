cart = []

while True:
    choice = input("to add the items to cart type 'yes': ")
    if choice == "yes":
        item = input("enter the item name to add to the cart: ")
        cart.append(item)
        print(f"the current items in the cart are {cart}")
    else:
        break