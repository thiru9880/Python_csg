def add(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

source = [1,2,3,4,5,6]
result = add(source)
print(result)    
