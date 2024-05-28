while True:
    with open("name.txt", "a") as file:
        names = input("enter the names to file: ")
        file.write(names+'\n')
        choice = input("do you want to add more names, type (y/n): ")
        if choice == "n":
            break

with open("name.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip().capitalize())
