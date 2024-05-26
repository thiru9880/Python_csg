products = [
    {"name": "Smartphone", "price": 500, "description": "A handheld device used for communication and browsing the internet."},
    {"name": "Laptop", "price": 1000, "description": "A portable computer that is easy to carry around."},
    {"name": "Headphones", "price": 50, "description": "A pair of earphones worn over the head to listen to music."},
    {"name": "Smartwatch", "price": 300, "description": "A wearable device used for fitness tracking and receiving notifications."},
    {"name": "Bluetooth speaker", "price": 100, "description": "A portable speaker that connects wirelessly to devices using Bluetooth technology."}
]
cart = []

while True:
    choice = input("do you want to continue shoping type 'yes' to continue: ")

    if choice == "yes":
        print("below is the list of the product")
        for index,product in enumerate(products):
            print(f"{index} : {"name"} : {"price"} : {"description"} ")
        product_id = int(input("enter the product id: "))

        if products[product_id] in cart:
            products[product_id]["quantity"] += 1
        else:
            products[product_id]["quantity"] = 1
            cart.append(products[product_id])

        total = 0
        print(f"the selected items in the cart are {cart}")
        for product in cart:
            print(f"name: {product["name"]} : price ${product["price"]} : QTY '{product["quantity"]}' no's")
            total = total + product["price"] * product["quantity"]
        print(f"the total cart value is {total}")
    else:
        break

            

