def remove_duplicate(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

ids = [1,2,3,4,5,2,4,6,7,3,8,9,1]
result = remove_duplicate(ids)
print(result)


def remove_dupli(numbers):
    new_list = list(set(numbers))
    return new_list

resul= remove_dupli(ids)
print(resul)