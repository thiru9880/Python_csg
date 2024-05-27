n = 10
d = 5
result = 0

try:
    result = n/d
except ZeroDivisionError:
    print("cannot devide a number by zero")
else:
    print(result)

finally:
    print("this code will be excuited no matter ")