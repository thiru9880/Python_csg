def add(*args):
    sum = 1
    for n in args:
        sum *= n
    return sum

print(add(1,2,3,4,5))