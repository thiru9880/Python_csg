products = ["iphone", "ipad", "imac"]
#displaying current products

print(f"the available items in the products: {products} inthe store")

# items to remove
remove_item= input("enter the product to remove: ")

products.remove(remove_item)

print(f"the available items in the products: {products} inthe store")

# products to add

add_item = input("enter the item to add: ")
products.append(add_item)

print(f"the available items in the products: {products} inthe store")