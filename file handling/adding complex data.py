def save_user_data():
    name = input("enter the name: ")
    email = input("enter the email: ")
    contact = input("enter the contact: ")

    user_data = f"name: {name}\nemail: {email}\ncontact: {contact}\n"
    with open("user.txt", "a") as file:
        file.write(user_data)

    with open("user.txt", "r") as file:
        lines= file.readlines()
        for line in lines:
            print(line.strip())

save_user_data()