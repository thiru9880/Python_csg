products = ["iphone", "ipad", "imac"]

print(f"the available products are: {products}")

add_item = input("enter the item to add: ")

add_after = input(f"after which product you want to add {add_item} : ")

index = products.index(add_after)

products.insert(index+1, add_item)

print(f"the available products are: {products}")