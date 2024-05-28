n = 10
d = 0
result = 0

try:
    result = n/d
except ZeroDivisionError:
    print("cannot devide a number by zero")
print(result)