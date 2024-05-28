while True:
    with open("name.txt", "a") as file:
        name = input("enter the name to add to the file: ")
        file.write(name+'\n')
        choice = input("do you want to add more names, type (y/n): ")
        if choice == "n":
            break