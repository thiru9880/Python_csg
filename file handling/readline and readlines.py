# with open("data.txt", "r") as file:
#     line1 = file.readline()
#     line2 = file.readline()
# print(line1)
# print(line2)

with open("data.txt", "r") as file:
    lines = file.readlines()
print(lines)


for line in lines:
    print(line)