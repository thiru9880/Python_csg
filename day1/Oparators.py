# Types of Oparetors
''' A oparetor is a symbol that perform certain oparation between operands
* Arthemetic Oparetors (+, - , * , % , / , **)
* Relational/ Comparisan Oparator (==, !=, <, >, <=, >=)
* Assainment Oparetors (=, +=, -=, *=, /=, %=, **=)
* Logical Oparetors (or, not, and)'''
# a = 2
# b = 3
# sum = a+b
# print(sum)

# a = 10
# b = 20

# print((a==b) and (a<b))
# print((a==b) or (a<b))
# print((a!=b) or (a<b))
# print((a!=b) and (a<b))

"""Type casting and type conversion
Type conversion is defult in python and type casting is a manual changes"""

# example 
# a = 4 
# b = 6.34
# print(a+b)  # In this senario python will convert int to float the output is 10.34
 
#  # example 2
 
# c = "4"
# d = 6 
# print(int(c)+d) # hear we need to convert str in to int manually other wise we will get the error this is called type casting

# name = str(input("Name is:"))
# age = int(input("Age:"))
# marks = int(input("marks:"))

# print("name is:", name)
# print("age", age)
# print("marks:", marks)

a = int(input("enter the value a:"))
b = int(input("enter the value B: "))
print(a>=b)
