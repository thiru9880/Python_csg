def chocolate():
    print("chocolate")

def decorators(func):
    def wrapper(*args,**kmargs):
        print("wrapper up side")
        func(*args,**kmargs)
        print("wrapper down side")
    return wrapper

chocolate = decorators(chocolate)
chocolate()

# or use @decorator
@decorators
def cake(name):
    print("cake"+" "+ name)

cake("apple")