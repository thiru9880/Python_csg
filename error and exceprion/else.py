n = 10
d = 2


try:
    result = n/d
except ZeroDivisionError:
    print("cannot devide a number by zero")
else:
    print(result)