def product(**kwargs):
    for key,value in kwargs.items():
        print(key+":"+value)

product(name= "iphone", price="300")
product(name="ipad", price="200")