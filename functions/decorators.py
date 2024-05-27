def chocolate():
    print("chocolate")

def decorators(func):
    def wrapper():
        print("wrapper up side")
        func()
        print("wrapper down side")
    return wrapper

chocolate = decorators(chocolate)
chocolate()

# or use @decorator
@decorators
def cake():
    print("cake")

cake()