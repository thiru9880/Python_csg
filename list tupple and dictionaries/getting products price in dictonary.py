products = {"iphone": 400, "imac": 600, "ipad": 300 }

print(products)
# # displaying the product price
product = input("ener the product name for the price details: ")

# print(f"the price of the product {product} is {products[product]}")

# # adding the new product 
new_product = input("enter the new product name: ")

product_price= input(f"enter the new product price of product {new_product}: ")
products[new_product] = product_price

print(f"the new product is add and the updated products are {products}")

#deleting the product

deleting_product = input("enter the product to delete: ")
del products[deleting_product]

print(f"the product {deleting_product} is deleted, the updated list of the products is {products}")